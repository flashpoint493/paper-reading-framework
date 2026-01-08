# 一键发布脚本 - GitHub 和 PyPI

Write-Host "=== 一键发布脚本 ===" -ForegroundColor Cyan
Write-Host ""

$GITHUB_USERNAME = "ocarina1024"
$REPO_NAME = "paper-reading-framework"
$GITHUB_URL = "https://github.com/${GITHUB_USERNAME}/${REPO_NAME}.git"

# GitHub 发布
Write-Host "=== GitHub 发布 ===" -ForegroundColor Yellow
Write-Host ""

try {
    $remoteUrl = git remote get-url origin 2>$null
    if ($remoteUrl) {
        Write-Host "远程仓库已设置: $remoteUrl" -ForegroundColor Green
    }
} catch {
    Write-Host "添加远程仓库..." -ForegroundColor Yellow
    git remote add origin $GITHUB_URL
}

$currentBranch = git branch --show-current
if ($currentBranch -eq "master") {
    Write-Host "重命名分支 master -> main" -ForegroundColor Yellow
    git branch -M main
}

Write-Host "尝试推送到 GitHub..." -ForegroundColor Yellow
git push -u origin main 2>&1 | Out-String

if ($LASTEXITCODE -eq 0) {
    Write-Host "GitHub 推送成功！" -ForegroundColor Green
    Write-Host "仓库地址: $GITHUB_URL" -ForegroundColor Cyan
} else {
    Write-Host "GitHub 推送失败，请先在 GitHub 创建仓库" -ForegroundColor Red
    Write-Host "访问: https://github.com/new" -ForegroundColor Cyan
    Write-Host "仓库名: $REPO_NAME" -ForegroundColor Cyan
}

Write-Host ""
Write-Host "=== PyPI 发布 ===" -ForegroundColor Yellow
Write-Host ""

if (-not (Test-Path "dist\paper_reading_framework-0.1.0-py3-none-any.whl")) {
    Write-Host "构建 Python 包..." -ForegroundColor Yellow
    python -m pip install --upgrade build twine --quiet
    python -m build
}

Write-Host "检查包..." -ForegroundColor Yellow
twine check dist/*

$pypiToken = $env:PYPI_API_TOKEN
if (-not $pypiToken) {
    Write-Host ""
    Write-Host "需要 PyPI API Token" -ForegroundColor Yellow
    Write-Host "获取: https://pypi.org/manage/account/token/" -ForegroundColor Cyan
    $pypiToken = Read-Host "请输入 PyPI API Token (或按 Enter 跳过)"
}

if ($pypiToken) {
    Write-Host "上传到 PyPI..." -ForegroundColor Yellow
    $env:TWINE_USERNAME = "__token__"
    $env:TWINE_PASSWORD = $pypiToken
    twine upload dist/*
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "PyPI 发布成功！" -ForegroundColor Green
        Write-Host "包地址: https://pypi.org/project/paper-reading-framework/" -ForegroundColor Cyan
    }
    
    Remove-Item Env:TWINE_USERNAME -ErrorAction SilentlyContinue
    Remove-Item Env:TWINE_PASSWORD -ErrorAction SilentlyContinue
} else {
    Write-Host "跳过 PyPI 发布" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "=== 完成 ===" -ForegroundColor Green
