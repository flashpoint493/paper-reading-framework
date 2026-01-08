"""
Paper Skill 使用示例
演示如何在 Cursor 等 AI IDE 中使用论文阅读技能
"""

from paper_skill import PaperSkill

# ============================================
# 示例 1: 一键下载和分析论文
# ============================================
def example_download_and_analyze():
    """下载并完整分析一篇论文"""
    skill = PaperSkill()
    
    # 使用 arXiv ID
    result = skill.download_and_analyze("2301.12345")
    
    if result.get("success"):
        print("✓ 分析完成！")
        print(f"  笔记: {result['note_path']}")
        print(f"  代码: {result['code_dir']}")
        print(f"  摘要: {result['summary_path']}")
    else:
        print(f"✗ 失败: {result.get('error')}")


# ============================================
# 示例 2: 快速获取摘要
# ============================================
def example_quick_summary():
    """快速获取论文摘要（不保存文件）"""
    skill = PaperSkill()
    
    summary = skill.quick_summary("2301.12345")
    print("论文摘要:")
    print(summary)


# ============================================
# 示例 3: 仅下载论文
# ============================================
def example_download_only():
    """仅下载论文，不进行分析"""
    skill = PaperSkill()
    
    paper_path = skill.download_paper("2301.12345")
    if paper_path:
        print(f"✓ 下载成功: {paper_path}")
    else:
        print("✗ 下载失败")


# ============================================
# 示例 4: 分析已有论文
# ============================================
def example_analyze_existing():
    """分析已下载的论文"""
    skill = PaperSkill()
    
    # 分析已有论文
    result = skill.analyze_paper(
        "papers/2301.12345/paper.pdf",
        analysis_type="summary"
    )
    
    if "error" not in result:
        print("分析结果:")
        print(result["analysis"])
    else:
        print(f"分析失败: {result['error']}")


# ============================================
# 示例 5: 批量处理多篇论文
# ============================================
def example_batch_process():
    """批量处理多篇论文"""
    skill = PaperSkill()
    
    paper_ids = [
        "2301.12345",  # XPBI
        "2301.12345",  # VR-GS
        "2301.12345",  # 其他论文
    ]
    
    results = []
    for paper_id in paper_ids:
        print(f"\n处理论文: {paper_id}")
        result = skill.download_and_analyze(paper_id)
        results.append((paper_id, result))
        
        if result.get("success"):
            print(f"✓ 完成")
        else:
            print(f"✗ 失败: {result.get('error')}")
    
    # 汇总结果
    print("\n" + "=" * 60)
    print("批量处理完成")
    print("=" * 60)
    for paper_id, result in results:
        if result.get("success"):
            print(f"✓ {paper_id}: {result['note_path']}")
        else:
            print(f"✗ {paper_id}: {result.get('error')}")


# ============================================
# 主函数
# ============================================
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("使用方法:")
        print("  python example_skill_usage.py download_and_analyze")
        print("  python example_skill_usage.py quick_summary")
        print("  python example_skill_usage.py download_only")
        print("  python example_skill_usage.py analyze_existing")
        print("  python example_skill_usage.py batch_process")
        sys.exit(1)
    
    action = sys.argv[1]
    
    if action == "download_and_analyze":
        example_download_and_analyze()
    elif action == "quick_summary":
        example_quick_summary()
    elif action == "download_only":
        example_download_only()
    elif action == "analyze_existing":
        example_analyze_existing()
    elif action == "batch_process":
        example_batch_process()
    else:
        print(f"未知操作: {action}")
