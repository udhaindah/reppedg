# Layeredge 多账号注册免费 Python Bot

此 Python Bot 脚本可使用指定的 HTTP 代理同时管理多个 Layeredge 注册账户，处理认证并在与服务器建立的连接之间保持持久会话。

## 功能特点

- 使用代理创建账户，确保安全（#Safu）。
- 支持自定义邀请链接（Referrals Code），并可同时使用多个邀请码。
- 所有日志均保存在 `response.txt` 文件中。

# 如何配置 Layeredge 邀请链接

1. 打开 `run.py` 文件，在第 `10` 行 [添加你想使用的邀请链接码](https://github.com/Solana0x/layeredge/blob/5387d518f7aa27cb0725be59767e07497814553d/run.py#L10)。

## 运行步骤

在运行脚本之前，确保已经在你的计算机上安装了 Python。然后使用以下命令安装所需的 Python 包：

1. 克隆仓库：```git clone https://github.com/Solana0x/layeredge.git```
2. 进入目录：```cd layeredge```
3. 安装依赖：```pip install -r requirements.txt```
4. 获取邀请链接（Refferal Codes），如果需要生成私钥和公钥，请运行 ```python key.py```。
5. 在 `proxy.txt` 文件中添加多个代理（可添加上千条），格式示例：`http://username:pass@ip:port`。
6. 执行命令 ```python run.py``` 以注册账户。

## 环境要求

- 邀请链接 Nodepay 账户（ [https://t.co/QnbzgXDCXX](https://t.co/QnbzgXDCXX) ）
- 安装了 Python （从 [https://www.python.org/downloads/](https://www.python.org/downloads/) 安装或在 Ubuntu 上使用 `sudo apt install python3`）
- VPS 服务器（可使用 AWS Free Tier、Google Free Tier、Gitpod 或其他，每月约 2-5 美元）
- 代理服务器（建议购买 DataCenter 代理来批量创建账户）

# NstProxy - [https://app.nstproxy.com/register?i=SkKXHm](https://app.nstproxy.com/register?i=SkKXHm)

![image](https://github.com/user-attachments/assets/8e1466d1-e71d-414f-b357-53eef4ea00d8)

## 如需帮助，请联系：`0xphatom` (Discord: [https://discord.com/users/979641024215416842](https://discord.com/users/979641024215416842))

# 社交平台 

- Telegram: [https://t.me/phantomoalpha](https://t.me/phantomoalpha)  
- Discord: [https://discord.gg/pGJSPtp9zz](https://discord.gg/pGJSPtp9zz)
