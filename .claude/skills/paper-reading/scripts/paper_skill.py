#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Paper Reading Skill - Main entry point for paper download and analysis
Usage: python paper_skill.py <arxiv_id_or_url> [--action <action>] [--type <type>]
"""

import sys
import os
from pathlib import Path

# Add project root to path
script_dir = Path(__file__).parent
project_root = script_dir.parent.parent.parent.parent
sys.path.insert(0, str(project_root))

# Try to import from original structure
try:
    from src.paper.fetcher import PaperFetcher
    from src.paper.parser import PaperParser
    from src.api.moonshot_client import MoonshotClient
    from src.knowledge.internalizer import KnowledgeInternalizer
    from src.implementation.code_generator import CodeGenerator
except ImportError:
    # If import fails, try to find the modules in original_code
    original_code_path = project_root / "original_code"
    if original_code_path.exists():
        sys.path.insert(0, str(original_code_path))
        from src.paper.fetcher import PaperFetcher
        from src.paper.parser import PaperParser
        from src.api.moonshot_client import MoonshotClient
        from src.knowledge.internalizer import KnowledgeInternalizer
        from src.implementation.code_generator import CodeGenerator
    else:
        print("Error: Cannot find paper reading framework modules")
        sys.exit(1)


class PaperSkill:
    """Paper Reading Skill - Unified API interface"""
    
    def __init__(self, config_path=None):
        """Initialize skill
        
        Args:
            config_path: Config file path (default: project root config.yaml)
        """
        if config_path is None:
            config_path = str(project_root / "config.yaml")
        
        self.config_path = config_path
        self.fetcher = PaperFetcher(config_path=config_path)
        self.parser = PaperParser()
        self.client = MoonshotClient(config_path=config_path)
        self.internalizer = KnowledgeInternalizer(config_path=config_path)
        self.code_generator = CodeGenerator(config_path=config_path)
    
    def download_and_analyze(self, arxiv_id: str) -> dict:
        """
        Download paper and run complete analysis (one-click operation)
        
        Args:
            arxiv_id: arXiv ID or URL (e.g., "2301.12345" or "https://arxiv.org/abs/2301.12345")
        
        Returns:
            Dictionary containing all generated file paths
        """
        print(f"Starting paper processing: {arxiv_id}")
        print("=" * 60)
        
        # 1. Download paper
        print("\n[1/5] Downloading paper...")
        paper_path = self.fetcher.download_arxiv_paper(arxiv_id)
        if not paper_path:
            return {"error": "Paper download failed"}
        
        print(f"Paper downloaded: {paper_path}")
        
        # 2. Parse paper
        print("\n[2/5] Parsing paper...")
        paper_info = self.parser.parse_pdf(str(paper_path))
        if not paper_info:
            return {"error": "Paper parsing failed"}
        
        paper_id = Path(paper_path).parent.name
        print(f"Paper title: {paper_info.get('title', 'Unknown')}")
        print(f"Paper ID: {paper_id}")
        
        # 3. AI Analysis
        print("\n[3/5] AI deep analysis...")
        paper_content = paper_info.get("full_text", "") or paper_info.get("abstract", "")
        if not paper_content:
            # Try using arXiv URL for analysis
            arxiv_url = f"https://arxiv.org/abs/{arxiv_id}" if not arxiv_id.startswith("http") else arxiv_id
            analysis = self.client.analyze_paper(arxiv_url, analysis_type="comprehensive", paper_url=arxiv_url)
        else:
            analysis = self.client.analyze_paper(paper_content, analysis_type="comprehensive")
        
        key_points = self.client.extract_key_points(paper_content or arxiv_id)
        implementation_guide = self.client.generate_implementation_guide(paper_content or arxiv_id)
        
        # 4. Knowledge Internalization
        print("\n[4/5] Knowledge internalization...")
        note_path = self.internalizer.create_note(paper_info, analysis, key_points, paper_id=paper_id)
        summary_content = self.internalizer.create_summary(paper_info, analysis)
        summary_path = self.internalizer.get_summaries_dir(paper_id=paper_id, paper_info=paper_info) / f"{paper_id}_summary.md"
        summary_path.write_text(summary_content, encoding="utf-8")
        
        # Update knowledge graph
        entry = self.internalizer.create_knowledge_graph_entry(paper_info, key_points)
        self.internalizer.save_knowledge_graph([entry], paper_id=paper_id, paper_info=paper_info)
        
        # 5. Code Generation
        print("\n[5/5] Generating code project...")
        code_dir = self.code_generator.create_project_structure(
            paper_info.get("title", "Unknown"),
            implementation_guide,
            language="python",
            paper_id=paper_id
        )
        self.code_generator.save_implementation_guide(
            paper_info.get("title", "Unknown"),
            implementation_guide,
            paper_id=paper_id
        )
        
        # Return results
        result = {
            "success": True,
            "paper_id": paper_id,
            "paper_path": str(paper_path),
            "note_path": str(note_path) if note_path else None,
            "summary_path": str(summary_path) if summary_path else None,
            "code_dir": str(code_dir) if code_dir else None,
            "knowledge_graph_path": str(self.internalizer.knowledge_dir / "knowledge_graph.json"),
        }
        
        print("\n" + "=" * 60)
        print("Processing complete!")
        print("=" * 60)
        print(f"Notes: {result['note_path']}")
        print(f"Summary: {result['summary_path']}")
        print(f"Code: {result['code_dir']}")
        
        return result
    
    def download_paper(self, arxiv_id: str):
        """
        Download paper only
        
        Args:
            arxiv_id: arXiv ID or URL
        
        Returns:
            Downloaded file path
        """
        return self.fetcher.download_arxiv_paper(arxiv_id)
    
    def analyze_paper(self, paper_path: str, analysis_type: str = "comprehensive") -> dict:
        """
        Analyze existing paper
        
        Args:
            paper_path: Paper file path
            analysis_type: Analysis type ("comprehensive", "summary", "innovation", "implementation")
        
        Returns:
            Analysis results
        """
        paper_info = self.parser.parse_pdf(paper_path)
        if not paper_info:
            return {"error": "Paper parsing failed"}
        
        paper_content = paper_info.get("full_text", "") or paper_info.get("abstract", "")
        if analysis_type == "comprehensive":
            analysis = self.client.analyze_paper(paper_content, analysis_type="comprehensive")
            key_points = self.client.extract_key_points(paper_content)
            implementation_guide = self.client.generate_implementation_guide(paper_content)
            return {
                "analysis": analysis,
                "key_points": key_points,
                "implementation_guide": implementation_guide,
            }
        else:
            analysis = self.client.analyze_paper(paper_content, analysis_type=analysis_type)
            return {"analysis": analysis}


def main():
    """Command line entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Paper Reading Skill - Quick download and analysis")
    parser.add_argument("arxiv_id", help="arXiv ID or URL")
    parser.add_argument("--action", choices=["download", "analyze", "full"], 
                       default="full", help="Action type (default: full)")
    parser.add_argument("--type", choices=["comprehensive", "summary", "innovation", "implementation"],
                       help="Analysis type (for analyze action)")
    
    args = parser.parse_args()
    
    skill = PaperSkill()
    
    if args.action == "download":
        result = skill.download_paper(args.arxiv_id)
        if result:
            print(f"Download successful: {result}")
        else:
            print("Download failed")
    elif args.action == "analyze":
        # Need to download first
        paper_path = skill.download_paper(args.arxiv_id)
        if not paper_path:
            print("Download failed")
            return
        result = skill.analyze_paper(str(paper_path), args.type or "comprehensive")
        print(result)
    else:  # full
        result = skill.download_and_analyze(args.arxiv_id)
        if result.get("error"):
            print(f"Error: {result['error']}")
        else:
            print("\nProcessing successful!")


if __name__ == "__main__":
    main()
