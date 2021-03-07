---
git基本操作
date: 2021 03 06 16:36
---

#### 上传文件

1. git add* 将工作区所有文件上传至暂存区

   ```
   git add*
   ```

2. git status  查看提交状态

   ```
   git status
   ```

3. git commit -m"提示信息"     将文件提交到本地仓库,并写上提示信息

   ```
   git commit -m'提示信息'          #-m'提示信息' 这个必须写
   ```

4. git push  上传到github仓库

   ```
   git push
   ```

   

#### 版本回退操作

1. 首先查看版本

   ```
   git log					#查看版本详细信息
   git log --pretty=oneline		#查看精简版后的版本信息
   ```

2. 回退

   ```
   git reset --hard 提交编号	#每个版本前都有编号
   ```

3. 想回到之前最新的状态

   ```
   git reflog
   git reset --hard 提交编号
   ```

   





