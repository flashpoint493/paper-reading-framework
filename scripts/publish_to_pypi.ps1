# PyPI 发布脚本 (PowerShell)

Write-Host "=== PyPI 发布脚本 ===" -ForegroundColor Cyan
Write-Host ""

# 检查构建工具
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "错误: 未找到 python 命令" -ForegroundColor Red
    exit 1
}

# 安装/更新构建工具
Write-Host "安装构建工具..." -ForegroundColor Yellow
python -m pip install --upgrade build twine --quiet

# 清理旧的构建文件
Write-Host "清理旧的构建文件..." -ForegroundColor Yellow
if (Test-Path build) { Remove-Item -Recurse -Force build }
if (Test-Path dist) { Remove-Item -Recurse -Force dist }
Get-ChildItem -Filter "*.egg-info" -Recurse | Remove-Item -Recurse -Force

# 构建包
Write-Host "构建 Python 包..." -ForegroundColor Yellow
python -m build

# 检查包
Write-Host ""
Write-Host "检查包..." -ForegroundColor Yellow
twine check dist/*

Write-Host ""
Write-Host "=== 构建完成 ===" -ForegroundColor Green
Write-Host ""
Write-Host "下一步：" -ForegroundColor Cyan
Write-Host "1. 测试上传到 TestPyPI:"
Write-Host "   twine upload --repository testpypi dist/*"
Write-Host ""
Write-Host "2. 发布到 PyPI:"
Write-Host "   twine upload dist/*"
Write-Host ""
Write-Host "注意：需要 PyPI API token（格式: pypi-xxx）" -ForegroundColor Yellow
Write-Host "获取地址: https://pypi.org/manage/account/token/" -ForegroundColor Cyan
