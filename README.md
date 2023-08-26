# OpenAI Service@GAIR

为了解决大陆无法使用OpenAI API服务的问题，实验室内部搭建了可以在任意环境使用OpenAI API服务的Server，具体可以参加如下例子；


# Example

### 1. 简单chatgpt调用
[参考代码](./examples/chatgpt.py)

```shell
export OPENAI_API_KEY = XXXXX
python chatgpt.py
```

### 2. 支持多个样本并行处理的chatgpt调用实例
[参考代码](./examples/chatgpt_batch.py)

```
export OPENAI_API_KEY = XXXXX
python chatgpt_batch.py
```






# Deployment

使用aws搭建自己的openai服务。我们参考和使用了[openai-forward项目](https://github.com/beidongjiedeguang/openai-forward/).

首先，我们必须在aws上创建一个服务器。在本项目中，服务器`ip = 34.195.96.131`，域名`openai.plms.ai`。然后，我们在该服务器上运行以下命令
```shell
pip install openai-forward
openai_forward run   # 运行
```
第二个命令可以参考以下命令行参数，我们**只需指定端口`--port`即可**：
### 命令行参数
可通过 `openai-forward run --help` 查看

<details open>
  <summary>Click for more details</summary>

**`openai-forward run`参数配置项**

| 配置项 | 说明                |          默认值           |
|-----------------|-------------------|:----------------------:|
| --port | 服务端口号             |          8000          |
| --workers | 工作进程数             |           1            |
| --base_url | 同 OPENAI_BASE_URL | https://api.openai.com |
| --api_key | 同 OPENAI_API_KEY  |         `None`         |
| --forward_key | 同 FORWARD_KEY     |         `None`         |
| --route_prefix | 同 ROUTE_PREFIX    |          `None`          |
| --log_chat | 同 LOG_CHAT        |        `False`         |

通过上述设置，我们即可在服务器上运行openai API服务。我们可以在任意一台电脑设备上运行以下命令(可使用ip或者域名)，来获取openai API的回答：
```shell
# 通过ip访问
curl http://34.195.96.131/v1/chat/completions\
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Hello!"}]
}'
```
```shell
# 通过域名访问
curl http://openai.plms.ai/v1/chat/completions\
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Hello!"}]
}'
```

