"""
测试 Moonshot AI API 连接
"""

import sys
from pathlib import Path

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.api.moonshot_client import MoonshotClient


def test_api():
    """测试 API 连接"""
    print("=" * 60)
    print("测试 Moonshot AI API 连接")
    print("=" * 60)
    
    try:
        # 初始化客户端
        print("\n1. 初始化 API 客户端...")
        client = MoonshotClient()
        print("   [OK] 客户端初始化成功")
        print(f"   - API 端点: {client.base_url}")
        print(f"   - 模型: {client.model}")
        
        # 测试简单对话
        print("\n2. 测试 API 调用...")
        messages = [
            {
                "role": "system",
                "content": "你是一个专业的学术论文分析助手。"
            },
            {
                "role": "user",
                "content": "请用一句话介绍你自己。"
            }
        ]
        
        response = client.chat_completion(messages)
        content = response["choices"][0]["message"]["content"]
        usage = response.get("usage", {})
        
        print("   [OK] API 调用成功！")
        print(f"\n   响应内容: {content}")
        print(f"\n   Token 使用:")
        print(f"   - Prompt tokens: {usage.get('prompt_tokens', 'N/A')}")
        print(f"   - Completion tokens: {usage.get('completion_tokens', 'N/A')}")
        print(f"   - Total tokens: {usage.get('total_tokens', 'N/A')}")
        
        print("\n" + "=" * 60)
        print("[OK] API 配置成功，可以开始使用了！")
        print("=" * 60)
        print("\n下一步:")
        print("1. 运行: python src/main.py fetch  (测试 SIGGRAPH 信息获取)")
        print("2. 运行: python src/main.py full papers/your_paper.pdf  (完整流程)")
        
        return True
        
    except ValueError as e:
        print(f"\n[ERROR] 配置错误: {e}")
        print("\n请检查:")
        print("1. .env 文件中是否设置了 MOONSHOT_API_KEY")
        print("2. 或者在 config.yaml 中配置了 api_key")
        return False
        
    except Exception as e:
        print(f"\n[ERROR] API 调用失败: {e}")
        print("\n可能的原因:")
        print("1. API Key 无效或已过期")
        print("2. 网络连接问题")
        print("3. API 服务暂时不可用")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    test_api()
