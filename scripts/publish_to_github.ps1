# GitHub 发布脚本 (PowerShell)

# 设置变量（请根据实际情况修改）
$GITHUB_USERNAME = "ocarina1024"
$REPO_NAME = "paper-reading-framework"
$BRANCH = "main"

Write-Host "=== GitHub 发布脚本 ===" -ForegroundColor Cyan
Write-Host ""

# 检查是否已设置远程仓库
try {
    $remoteUrl = git remote get-url origin 2>$null
    if ($remoteUrl) {
        Write-Host "远程仓库已设置:" -ForegroundColor Yellow
        git remote -v
        Write-Host ""
        $update = Read-Host "是否要更新远程仓库 URL? (y/n)"
        if ($update -eq "y" -or $update -eq "Y") {
            git remote set-url origin "https://github.com/${GITHUB_USERNAME}/${REPO_NAME}.git"
        }
    }
} catch {
    Write-Host "添加远程仓库..." -ForegroundColor Yellow
    git remote add origin "https://github.com/${GITHUB_USERNAME}/${REPO_NAME}.git"
}

# 重命名分支为 main（如果当前是 master）
$currentBranch = git branch --show-current
if ($currentBranch -eq "master") {
    Write-Host "重命名分支 master -> main" -ForegroundColor Yellow
    git branch -M main
}

# 推送代码
Write-Host ""
Write-Host "推送代码到 GitHub..." -ForegroundColor Yellow
git push -u origin $BRANCH

Write-Host ""
Write-Host "完成！" -ForegroundColor Green
Write-Host "仓库地址: https://github.com/${GITHUB_USERNAME}/${REPO_NAME}" -ForegroundColor Cyan
