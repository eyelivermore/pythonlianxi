# 创建
* 1：先在本地创建一个空目录做为仓库
* 2：CD 进入目录
* 3：通过输入 git init 命令 把这个目录变成一个Git可以管理的仓库
        现当前目录下多了一个.git的目录

# 添加文件
* 把一个文件放到Git仓库只需要两步。

        第一步，用命令git add告诉Git，把文件添加到仓库：
        例子：git add gitlianxi.txt
        把gitlianxi.txt添加到仓库


* 第二步，用命令git commit告诉Git，把文件提交到仓库
       
        例子：git commit -m "学习git第一课"
        -m 后面是改动的说明

# 查看
* 要随时掌握工作区的状态，使用git status命令

* 用git diff可以查看修改内容

# 学习版本退回

* 撤销工作区修改

      git checkout --file(文件名)
      git checkout -- file命令中的--很重要，没有--，就变成了“切换到另一个分支”的命令

* 撤销缓存区的修改
 
 git reset HEAD <file>
 再用git checkout -- 文件名  撤销工作区的修改 
 这样整个世界都清静了

checkout(撤销工作的修改)
reset(撤销缓存区的修改)

# 查看日志


* 在Git中，我们用git log命令查看日志

# 切换版本

    回退到上一个版本就可以使用git reset命令：
    例子：git reset --hard HEAD^

* 回到已经退回的版本想回到原来的版本
  
      git reset --hard 1094a(这个是版本ID)
      版本ID可以在日志里面查看

* Git提供了一个命令git reflog用来记录你的每一次命令

# 分支
要想学习好Git 就要理解工作区，缓存区和分支  
git更多是在管理你的修改  
每一次修改都会被记录  
用git add命令提交到缓存区  
再用 git commit提交到分支  
每次修改，如果不用git add到暂存区，那就不会加入到commit中  

## 创建分支
 分支其实就是指针  

    git checkout -b <分支名>
    -b 代表创建并切换

    用switch更科学
    git switch -c dev创建并切换dev分支
    git switch master 切换到master分支

## 查看分支
***git branch***  
-r 查看本地和远程分支  
当前分支前面会标一个*号  

## 切换分支
**git checkout <分支名>**  
用switch更科学  
git switch master 切换到master分支

## 合并分支
git merge命令用于合并指定分支到当前分支  
**git merge <指定分支名>**  
merge命令是把 指定分支，合并到当前分支上

## 删除分支
git branch -d <需要删除分支名>  
-d 指删除


小结
Git鼓励大量使用分支：  
查看分支：git branch  
创建分支：git branch <name>  
或者 git switch -c <name>创建并切换分支  
切换分支：git checkout <name>或者git switch <name>  
创建+切换分支：git checkout -b <name>或者git switch -c <name>  
合并某分支到当前分支：git merge <name>  
删除分支：git branch -d <name>  

# 查看远程仓库

git remote -v

## 上传远程仓库
* 第一步：先在github上创建仓库 
* 第二步：把本在仓库推送到远程仓库   
使用 git remote add <本地仓库名> git@github.com:<自己的github账户 名>/<远程仓库名>.git  
把本地库的内容推送到远程，用git push命令，实际上是把当前分支master推送到远程

### 以后再有新文件更新可以用
* git push <仓库名> <分支名>

## 删除远程库

如果添加的时候地址写错了，或者就是想删除远程库   
可以用git remote rm <name>命令  
其实就是解除本地于远程库的关联
想删除远程库要登陆Github账号再删除

## 把别人的项目加载到自己的仓库
可以点Fork到自己的仓库

## 克隆远程仓库到本地
克隆命令
git clone 
git clone git@github.com:<账号>/<仓库名>.git


