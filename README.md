# python-exercise

> 关于python的面试题及leetcode题目代码实现

## 目录

## Python基础

### 文件操作

1. [写一个返回该文件夹中文件的路径,以及其包含文件夹中文件的路径的函数](interview_question/print_dir.py)

### 模块与包

1. [函数输入为年月日，输出这是该年的第几天](interview_question/get_date.py)

1. [打乱一个排好序的list对象alist？](interview_question/upset_a_list.py)

### 数据类型

1. [现有字典 d= {'a':24,'g':52,'i':12,'k':33}请按value值进行排序?](interview_question/sort_dicts.py)

1. [请反转字符串 "aStr"?](interview_question/reverse_str.py)

1. [将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}](interview_question/to_dicts.py)

1. [请按alist中元素的age由大到小排序](interview_question/sort_list.py)

1. 下面代码的输出结果将是什么？
    ```python
    list1 = ['a','b','c','d','e']
    print(list1[10:])
    ```
    代码将会输出[]， 不会产生IndexError错误， 就像所期望的那样，尝试用超出成员的个数的index来获取某个列表的成员。例如尝试获取list[10]和之后的成员，会导致IndexError。然而， 尝试获取列表的切片，开始的index超过了成员个数不会产生IndexError， 而是仅仅返回一个空列表。这成为特别让人恶心的疑难杂症， 因为运行的时候没有产生错误，导致BUG很难被追踪到。

1. [写一个列表生成式，产生一个公差为11的等差数列](interview_question/gen_list.py)

1. [给定两个列表，怎么找出他们相同的元素和不同的元素？(集合)](interview_question/different_list.py)

1. [请写出一段python代码实现删除list里面的重复元素？](interview_question/dif_sim.py)

### 企业面试题

1. Python新式类与经典类的区别？  
  a. Python里凡是继承了object的类都是新式类  
  b. Python3中只有新式类  
  c. Python2中继承object的类是新式类,没有写父类的是经典类  
  d. 经典类目前在Python中基本没有应用  

2. Python中内置数据结构有几种?  
  int, str, float, complex, long(Python3中没有, 只有无限精度的int)  
  list, tuple, set, dict  

3. Python中如何实现单例模式? 请写出至少两种实现方法  
    第一种方法:[使用装饰器](interview_question/singleton.py)  
    第二种方法:[使用基类new](interview_question/singleton.py), 是真正创建实例对象的方法,所以重写基类的new方法,以此保证创建对象的时候只生成一个实例  
    ~~第三种方法:[元类](interview_question/singleton.py), 元类是用于创建类对象的类,类对象创建实例对象时一定要调用call方法, 因此在调用call时候始终只创建一个实例即可,type是Python的元类~~

4. [反转一个整数，例如-123 --> -321](interview_question/reverse_int.py)

5. [设计实现遍历目录与子目录，抓取.py文件](interview_question/os_test.py)

6. [一行代码实现1-100之和](interview_question/one_line_add.py)

7. [Python-遍历列表时删除元素的正确做法](interview_question/del_list.py)

8. [字符串的操作题目](interview_question/str_operation.py)

9. 可变类型与比可变类型  
  a. 可变类型有list,dict, 不可变类型有tuple, number, string  
  b. 当进行修改操作时,可变类型传递的是内存中的地址,也就是说,直接修改内存中的值,并没有开辟新的内存  
  c. 不可变类型被修改时,并没有改变原来内存地址中的值,而是开辟一块新的内存,将原来地址中的之复制进去,对这块新开辟的内存中的值进行操作

10. is和==有什么区别?  
  is: 比较的是两个对象的id是否相等,也就是比较两对象是否为同一个实例对象.是否指向同一个内存地址  
  ==: 比较两个对象的内容/值是否相等, 默认会调用对象的eq()方法
  
11. [求出列表所有奇数并构造新列表 ](interview_question/odd_number.py)

12. Python中变量的作用域?(变量查找顺序)  
    函数作用域的LEGB顺序  
    a. 什么是LEGB?  
    L: local函数内部作用域   
    E: enclosing 函数内部与内嵌函数之间  
    G: global全局作用域  
    B: build-in 内置作用域  
    python在函数中的查找分为4种, 称之为LEGB,也正是按照这种顺序来查找的  
    
13. [字符串 "123" 转换成 123，不使用内置api，例如 int()](interview_question/atoi.py)

14. [相加值为给定的某个数](interview_question/sum_is_target.py)  
    给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。示例:给定nums = [2,7,11,15],target=9 因为 nums[0]+nums[1] = 2+7 =9,所以返回[0,1]

15. [给列表中的字典排序](interview_question/sort_dicts2.py)  
    假设有如下list对象， ```alist=[{"name":"a","age":20},{"name":"b","age":30},{"name":"c","age":25}]``` ,
    将alist中的元素按照age从大到小排序 ```alist=[{"name":"a","age":20},{"name":"b","age":30},{"name":"c","age":25}]```

16. [python代码实现删除一个list里面的重复元素](interview_question/dist_func.py)

17. [统计一个文本中单词频次最高的10个单词？](interview_question/highest_frequency.py)

1. [请写出一个函数满足以下条件](interview_question/get_even.py)  
    该函数的输入是一个仅包含数字的list,输出一个新的list，其中每一个元素要满足以下条件：  
    1、该元素是偶数  
    2、该元素在原list中是在偶数的位置(index是偶数)  

1. [使用单一的列表生成式来产生一个新的列表](interview_question/gen_list2.py)  
    该列表只包含满足以下条件的值，元素为原始列表中偶数切片

1. [用一行代码生成[1,4,9,16,25,36,49,64,81,100]](interview_question/gen_list3.py)

1. [输入某年某月某日，判断这一天是这一年的第几天？](interview_question/get_data_in_year.py)

1. [两个有序列表，l1,l2，对这两个列表进行合并不可使用extend](interview_question/merge_list.py)

1. [给定一个任意长度数组，实现一个函数](interview_question/up_stream.py)  
    让所有奇数都在偶数前面，而且奇数升序排列，偶数降序排序，如字符串'1982376455',变成'1355798642'

1. [写一个函数找出一个整数数组中，第二大的数](interview_question/get_second_big.py)

1. 阅读一下代码他们的输出结果是什么？

    ```python
    def multi():
        return [lambda x : i*x for i in range(4)]
    print([m(3) for m in multi()])
    ```

1. [统计一段字符串中字符出现的次数](interview_question/count_str.py)

1. super函数的具体用法和场景
   [使用super调用父类方法](https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p07_calling_method_on_parent_class.html)

## Python高级

### 元类

1. Python中类方法、类实例方法、静态方法有何区别？  
    - 类方法：是类对象的方法，在定义时需要在上方使用@classmethod进行装饰，形参为cls，表示类对象，类对象和实例对象都可调用
    - 类实例方法：是实例化对象的方法，只有实例对象可以调用，形参为self，指代对象本身
    - 静态方法：是一个任意函数，在其上方使用@staticmethod进行装饰，可以用对象直接调用，静态方法实际上跟该类没有太大关系

2. 遍历一个object的所有属性，并print每一个属性名？
    ```python
    class Car:
        def __init__(self,name,loss): # loss [价格，油耗，公里数]
            self.name = name
            self.loss = loss
        
        def getName(self):
            return self.name
        
        def getPrice(self):
            # 获取汽车价格
            return self.loss[0]
        
        def getLoss(self):
            # 获取汽车损耗值
            return self.loss[1] * self.loss[2]

    Bmw = Car("宝马",[60,9,500]) # 实例化一个宝马车对象
    print(getattr(Bmw,"name")) # 使用getattr()传入对象名字,属性值。
    print(dir(Bmw)) # 获Bmw所有的属性和方法
    ```
    输出
    ```python
    宝马
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'getLoss', 'getName', 'getPrice', 'loss', 'name']
    ```

3. 写一个类，并让它尽可能多的支持操作符?
    ```python
    class Array:
        __list = []
        
        def __init__(self):
            print ("constructor") 
        
        def __del__(self):
            print ("destruct")
        
        def __str__(self):
            return "this self-defined array class"
    
        def __getitem__(self,key):
            return self.__list[key]
        
        def __len__(self):
            return len(self.__list)
    
        def Add(self,value):
            self.__list.append(value)
        
        def Remove(self,index):
            del self.__list[index]
        
        def DisplayItems(self):
            print ("show all items---")
            for item in self.__list:
                print (item)
    ```
    
4. 介绍Cython，Pypy Cpython Numba各有什么缺点  
    **Cython:** Cython是让Python脚本支持C语言扩展的编辑器，Cython能够将Python+C混合编码的.pyx脚本转换为C代码,主要用于优化Python脚本性能或Python调用C函数库  
    
    **Pypy:** Pypy最重要的一点就是Pypy集成了JIT。同时针对CPython的缺点进行了各方面的改良，性能得到了很大的提升。了解JIT技术的人都应该对Pypy很有好感。Pypy的有点是对纯Python项目兼容性极好，几乎可以直接运行并直接获得性能提升(官方宣称的6.3倍，但实际上没感觉有这么多)；缺点就是对很多C语言库支持性不好，Pypy社区一直有相关讨论   
    
    **Numba:** Numba是一个库，可以在运行时将Python代码编译为本机机器指令，而不会强制大幅度改变普通的Python代码  
    
    通用性：在三个方案中，Cython和Numba的兼容性都非常好，而Pypy对于部分库的支持较差（如Numpy，Scipy）。  
    
    速度：这三种方案的速度相差不大，通常来说Cython要快于Pypy，尤其是对于部分C扩展。Pypy要快于Numba，但针对于纯数值计算的工作，Numba甚至还要快于Cython。  
    
    易用性：易用性最好的无疑是Pypy，Pypy是Python的解释器，我们针对纯Python使用Pypy，除了Pypy不支持的部分库外，不需要进行任何改动。然后是Numba，Numba的基本使用方法就是给函数加一个装饰器，易用性也很高，最后是Cython，因为Cython中需要使用Python+C混合编码，如果需要移植，代价会很大。总结：Pypy是非常理想的Python解释器，最大的瑕疵就是对部分库的兼容问题。Cython是一种Python + C的便利性组合，转为C编译的扩展执行效率非常高，但使用相对麻烦，移植CPython项目代价较高。Numba更适合针对性优化，效率高，并且不会大幅度的改变普通的Python代码。所以三者实在没法说谁最优秀，只是在不同的方向针对性及适用性更高。  

5. 请描述抽象类与接口类的区别和联系？  

    共同点： 
    - 都是上层的抽象层
    - 都不能被实例化
    - 都能包含抽象的方法，这些抽象的方法用于描述类具备的功能，但不提供具体的实现
    
    区别：
    - 在抽象类中可以写非抽象的方法，从而避免在子类中重复书写他们，这样可以提高代码的复用性，这是抽象类的优势；接口中只能有抽象的方法
    - 一个类只能继承一个直接父类，这个父类可以是具体的类也可以是抽象类；但一个类可以实现多个接口
     
6. Python中如何动态获取和设置对象的属性？  

    如果要获取一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法
    ```shell
    >>> dir('ABC')
    ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
    ```
    
### 内存管理与垃圾回收机制

1. 哪些操作会导致Python内存溢出，怎么处理？  
    内存泄露的原因主要有三种：
    - 所用到的C语言开发的底层模块中出现了内存泄露
    - 代码中用到了全局的list、dict或其他容器，不停地网这些容器中插入对象，而忘记在使用完之后进行删除回收
    - 代码中有“引用循环”，python垃圾处理机制无法进行回收
    
    [Python内存泄露调试指导思想](https://jackywu.github.io/articles/python%E5%86%85%E5%AD%98%E6%B3%84%E9%9C%B2%E8%B0%83%E8%AF%95%E6%8C%87%E5%AF%BC%E6%80%9D%E6%83%B3/)
     
2. 关于Python内存管理，下列说法错误的是  
    - 变量不必事先声明
    - 变量无需先创建和赋值而直接使用（错误）
    - 变量无需指定类型
    - 可以使用del释放资源
    
### Python的内存管理机制及调优手段？

内存管理机制：引用计数、垃圾回收、内存池

- 引用计数：引用计数是一种非常高效的内存管理手段，当一个Python对象被引用时其引用计数增加1，当其不再被一个变量引用时则计数减1，当引用计数等于0时对象被删除。弱引用不会增加引用计数
- 垃圾回收：
    - 引用计数是一种垃圾收集机制，而且也是一种最直观、最简单的垃圾收集技术。当Python的某个对象的引用技术将为0时，说明没有任何引用指向该对象，该对象就成为要被回收的垃圾了。比如某个新建对象，它被分配给某个引用，对象的引用计数变为1，如果引用被删除，对象的引用计数为0，那么该对象就可以被垃圾回收。不过出现循环引用的话，引用计数机制就不再起有效的作用了。
    - [标记清除](https://foofish.net/python-gc.html)

调优手段：
- 手动垃圾回收
- 调高垃圾回收阈值
- 避免循环引用

### 内存泄漏是什么？如何避免？

内存泄露指由于疏忽或错误造成程序未能释放已经不再使用的内存。内存泄露并非指内存在物理上的消失，而是应用程序分配某段内存后，由于设计错误，导致在释放该段内存之前就失去了对该段内存的控制，从而造成了内存的浪费。

有__del__()函数的对象间的循环引用是导致内存泄露的主凶。不使用一个对象时使用：del object来删除一个对象的引用计数就可以有效访问内存泄露问题。

通过Python扩展模块gc来查看不能回收的对象的详细信息

可以通过sys.getrefcount(obj)来获取对象的引用计数，并根据返回值是否为0来判断是否内存泄露

## 函数

### Python常见的列表推导式

[表达式 for 变量 in 列表] 或 [表达式 for 变量 in 列表 if 条件] 

### 简述read、readline、readlines的区别？

- read 读取整个文件
- readline 读取下一行
- readlines 读取整个文件到一个迭代器以供我们遍历

### 什么是Hash(散列函数)？

散列函数（英文：Hash function）又称散列算法、哈希函数，是一种从任何一种数据中创建小的数字“指纹”的方法。散列函数把消息或数据压缩成摘要，使得数据变小，将数据格式固定下来。该函数将数据打乱混合，重新创建一个叫做散列值的指纹。散列值通常用一个短的随机字母和数字组成的字符串来表达

### Python函数重载机制？

函数重载主要是为了解决两个问题：

1. 可变参数类型
2. 可变参数个数

另外， 一个基本的设计原则是，仅仅当两个函数除了参数个数可以不同外，其功能是完全相同的，此时才使用函数重载，如果两个函数的功能其实不同，那么不应当使用重载，而应当使用一个名字不同的函数。

对于情况1，函数功能相同，但参数类型不同，Python如何处理？答案是根本不需要处理，因为Python可以接受任何类型的参数，如果函数的功能相同，那么不同的参数类型在Python中很可能是相同的代码，没有必要做成两个不同函数。

对于情况2， 函数功能相同，但参数类型不同，Python如何处理？大家知道，答案就是缺省参数。对那些缺少的参数设定为缺省参数即可解决问题。因为你假设函数功能相同，那么缺少的参数终归是需要用到的。

鉴于情况1跟情况2都有了解决方案，Python自然就不需要函数重载了。

### [写一个函数找出一个整数数组中，第二大的数](interview_question/function/second_large.py)

### [手写一个判断时间的装饰器](interview_question/function/timecheck.py)



## LeetCode热门面试问题

### Array

1. [两个数相加的和等于某个数](leetcode/array/two_sum.py)

2. [将零放到最后](leetcode/array/move_zeros.py)

3. [找单个出现的值](leetcode/array/single_number.py)

4. [list的交集](leetcode/array/intersect.py)

5. [一个存在列表里的数,你将它加1(高精度加法)](leetcode/array/plus_one.py)

6. [不新建一个二维列表旋转图片](leetcode/array/rotate_image.py)

7. [买卖股票的最好时间及最大收益分析](leetcode/array/max_profit.py)

8. [列表中是否有重复的元素？](leetcode/array/contains_duplicate.py)

9. [列表挪位](leetcode/array/rotate_array.py)


### Strings

1. [不用额外的空间翻转字符串](leetcode/strings/reverse_string.py)

1. [翻转数字](leetcode/strings/reverse.py)

1. [自己实现strStr()找子串](leetcode/strings/my_strstr.py)

1. [报数](leetcode/strings/count_and_say.py)

1. [不一样的自己写的atoi()](leetcode/strings/my_atoi.py)

1. [找英文回文](leetcode/strings/valid_palindrome.py)

1. [找字符串中第一个不重复的字母](leetcode/strings/first_uniq_char.py)

1. [判断是不是用同样的字母构成的单词](leetcode/strings/valid_anagram.py)

### Linked List

1. [删除链表中的当前节点的元素](leetcode/linked_list/delete_node.py)

1. [删除链表中倒数第N个节点](leetcode/linked_list/remove_eth_from_end.py)

1. [有序链表合并](leetcode/linked_list/merge_two_lists.py)

1. [链表倒序](leetcode/linked_list/reverse_list.py)

1. [判断是否是回文链表](leetcode/linked_list/is_palindrome.py)

### Sorting and Searching

1. [合并有序列表](leetcode/sorting_and_searching/merge.py)

### Math

1. [3的次方](leetcode/math/is_power_of_three.py)

1. [三和五的倍数](leetcode/math/fizz_buzz.py)

### Other

1. [将一个整数转换为二进制并计算里面有多少个1](leetcode/other/hamming_weight.py)
1. [将两个整数转换为二进制并计算有多少位不一样](leetcode/other/hamming_distance.py)
1. [杨辉三角](leetcode/other/pascal_triangle.py)
1. [括号匹配](leetcode/other/valid_parentheses.py)
1. [将一个整数转换为二进制数并逆序](leetcode/other/reverse_bits.py)
1. [找到丢失的数](leetcode/other/missing_number.py)  
1. [罗马数字转换](leetcode/other/roman_to_integer.py)
1. [寻找n以下的质数](leetcode/math/count_primes.py)

## 参考文章

- [关于python的面试题](https://github.com/Niracler/python-interview-question)  
- [python-exercises](https://www.w3resource.com/python-exercises/)
