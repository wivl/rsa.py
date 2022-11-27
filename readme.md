# rsa.py

## 简介
一个 rsa 加密算法的 python 实现

此仓库仅仅是加密算法实现的一次练习，**请勿在任何重要场合使用此仓库进行加密和解密，否则，造成的后果将由使用者自己承担**


## 使用方法

### 密钥生成

首先需要 <code>private_key</code> 和 <code>private_key</code> 文件，仓库中已提供生成好的密钥对，您也可以自己生成:

```console
python3 key.py
```
默认生成 **最大为 2048 位的 p 和 q**，你也可以修改 <code>key.py</code> 中 <code>22</code> 行的 <code>KEY_LENGTH</code> 值。**注意：<code>KEY_LENGTH</code> 值为 2048 时在本机测试的时间开销在 7000s 左右**，其中的素数判断使用的是 [米勒-拉宾素性检验](https://zh.wikipedia.org/zh-cn/%E7%B1%B3%E5%8B%92-%E6%8B%89%E5%AE%BE%E6%A3%80%E9%AA%8C)。

### 加密

```console
python3 main.py -e input.txt output.bin
```
其中 <code>-e</code> 表示 加密，<code>input.txt</code> 可以不指定，默认为读取 <code>input.txt</code> 文件，加密到 <code>output.bin</code>

或者使用仓库提供的示例 <code>hamlet.txt</code>:

```console
python3 main.py -e hamlet.txt
```

### 解密

```console
python3 main.py -d output.bin decrypted.txt
```
其中 <code>-d</code> 表示 解密，<code>output.bin</code> 可以不指定，默认为读取 <code>output.bin</code> 文件，解密到 <code>decrypted.txt</code>

### 帮助

使用

```console
python3 main.py -h
```

获得帮助