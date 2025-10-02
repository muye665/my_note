## 容器

1. 序列容器：存储元素的序列，允许双向遍历。

   - std::vector：动态数组，支持快速随机访问。

   - std::deque：双端队列，支持快速插入和删除。

   - std::list：链表，支持快速插入和删除，但不支持随机访问。

2. 关联容器：存储键值对，每个元素都有一个键（key）和一个值（value），并且通过键来组织元素。

   - std::set：集合，不允许重复元素。

   - std::multiset：多重集合，允许多个元素具有相同的键。

   - std::map：映射，每个键映射到一个值。

   - std::multimap：多重映射，存储了键值对（pair），其中键是唯一的，但值可以重复，允许一个键映射到多个值。

3. 无序容器（C++11 引入）：哈希表，支持快速的查找、插入和删除。

   - std::unordered_set：无序集合。

   - std::unordered_multiset：无序多重集合。

   - std::unordered_map：无序映射。

   - std::unordered_multimap：无序多重映射。

## 内存四区模型

- 代码区：存放二进制代码，由系统管理
- 全局区：存放全局变量、静态变量和常量（const、字符串常量）
- 栈区：由编译器自动分配和释放
- 堆区：由程序员分配和释放  

- new关键字：在堆区开辟数据，返回的是该数据类型的指针

  ```c++
  int *p = new int(10);    //在堆区创建int数字10，指针p保存在栈区指向堆区的10
  int *arr = new int[10];  //在堆区创建长度为10的int数组，指针arr保存在栈区指向堆区的数组
  ```

- delete关键字

  ```c++
  delete p;
  delete[] arr;
  ```

  分别代表删除堆区的变量和数组

## 引用

- 基本语法

  `````c++
  int &b = a; // 数据类型 &别名 = 现名
  `````

  

- 注意事项

  - 引用必须要初始化

  - 引用初始化后，可以赋值，但不能更改引用（相当与指针的指向固定）

    ```c++
    int a = 10;
    int b = 20;
    int &c = a;
    c = b;      //正确，可以进行赋值操作
    int &c = b; //错误，不能更改已经定义的引用
    ```

    此时`a = b = c = 20`

- 引用可以作为函数参数

  ```c++
  void test(int &a, int& b){ //交换数字
  	temp = a;
      a = b;
      b = temp;
  }
  ```

- 引用可以作为函数返回值

  ```c++
  int& test(){
  	static int a = 10;
  	return a;
  }
  int main(){
      int& ref = test(); 				 //函数返回静态变量a
      std::cout << "ref = " << ref << std::endl;
      test() = 20;                     //函数的引用作为左值
      std::cout << "ref = " << ref << std::endl;
  }
  ```

  打印结果分别为`ref = 10`，` ref = 20`， 函数的引用的主要作用是作为左值

- 引用本质：**指针常量**

  ```c++
  int& ref = a;
  int* const ref = &a;
  ```

  这两者等价，指针的**指向**不可改，指针指向的**值**可改

- 常量引用

  ```c++
  void test(const int& a){
  	std::cout << a << std::endl
  }
  ```

  防止函数中的形参改变实参

- #### 左值引用与右值引用不同之处

  1. 左值引用引用左值，**左值可以修改**；右值引用引用右值，**右值不可以修改**
  2. 左值是由用户自定义变量组成，右值一般为编译器运行时开辟临时变量。

## 函数进阶

- 函数的默认参数

  ```c++
  int func(int a, int b = 10);
  ```

  默认值靠右

- 占位参数

  ```c++
  int func(int a, int);
  int main(){
  	func(10, 10);
  }
  ```

  调用函数时必须填补占位参数，但是占位参数可以有默认参数

  ```c++
  int func(int a, int = 10);
  ```

- 函数重载

  - 函数重载可以同时定义多个同名函数，但是**同名函数之间要有区别**（函数参数类型不同，或个数不同，或顺序不同，但是**函数返回值不可以作为区别之一**）语法

    ```c++
    void func(){
        std::count << "1" << std::endl;
    }
    void func(int a){  //函数重载
        std::count << "2" << std::endl;
    }
    int main(){
        func();
        func(10);
    }
    ```

    结果：`1` `2`

    作用：重载了函数func（调用重载函数时会自动检测传入参数类型，匹配对应的函数参数类型）

  - 注意事项
    - 函数重载可以同时定义多个同名函数，但是**同名函数之间要有区别**（函数参数类型（包括const）不同，或个数不同，或顺序不同，但是**函数返回值不可以作为区别之一**）
    - 当函数重载碰到默认参数，有二义性，会报错（写函数重载时尽量避免出现默认参数）

## 类和对象进阶

- 构造函数和析构函数()

  - 作用：对象的初始化和清理

  - 语法：

    ```c++
    class Person{
    public:
        Person(){}   //构造函数
        ~Person(){}  //析构函数
    };
    ```

    构造函数会在创建对象时自动调用，析构函数会在销毁对象时自动调用

  - 构造函数的分类

    ```c++
    class Person{
    public:
        Person(){}     			  //无参构造
        Person(int a){}           //有参构造
        Person(const Person& p){} //拷贝构造
    };
    //调用
    int main(){
        Person p1; 			//调用无参构造
        Person p2(10);		//调用有参构造
        Person p3(p2);		//调用拷贝构造
    }
    ```

  - 构造函数调用规则（不重要）

    - 用户没定义构造函数时，编译器会提供默认无参构造和默认拷贝构造
    - 用户定义了有参构造时，编译器会提供默认拷贝构造
    - 用户定义了拷贝构造时，编译器不会提供任何默认构造

  - 浅拷贝和深拷贝（不重要）
    - 编译器提供的默认的拷贝构造函数为浅拷贝
    - 浅拷贝缺点：对于指向堆区的指针，拷贝完后会有多个指针指向同一个堆区，这样会导致在使用析构函数释放堆区时，会因为多次释放同一片堆区而出错。深拷贝则会新建一片堆区让指针指
    - 至于深拷贝，是自己实现的......

- 初始化列表

  - 语法：

    ```c++
    class Person{
    public:
        Person(int a, int b): pa(a), pb(b){ //初始化类成员变量
            std::cout << "pa:" << pa << std::endl;
            std::cout << "pb:" << pb << std::endl;
        }
    private:
        int pa;
        int pb;
    };
    ```

- 类对象作为类成员

  - 例:

    ```c++
    class Phone{
    public:
        Phone(string pName){}
    };
    class Person{
    public:
        Person(string name, string p_name): preson_name(name), mPhone(p_name){
        }
    private:
        string person_name;
        Phone mPhone;  //类对象作为类成员
    };
    ```

    当其他类对象作为本类成员时，构造时**先构造其他类对象**，再构造自身。析构顺序相反

- 静态成员

  - 静态成员变量
    - 所有对象共享一份数据
    - 必须进行类外初始化
    - 在类外可直接通过类名进行访问（前提：静态成员为public）
  - 静态成员函数
    - 所有对象共享同一个函数
    - 静态成员函数只能访问静态成员变量

  ```c++
  class Person{
  public:
      static int number;   //静态成员变量
      static void func(){	 //静态成员函数
          std::cout << Person::number << std::endl;
      }
  };
  
  int Person::number = 100;  //静态成员变量类外初始化
  
  int main(){
      Person a;
      Person b;
      Person::func(); //调用静态成员函数
      std::cout << a.number << std::endl;  //结果为100
      b.number = 200;
      std::cout << a.number << std::endl;  //结果为200(所有对象共享一份数据)
      std::cout << Person::number << std::endl; //静态成员变量在类外可直接通过类名进行访问（前提：静态成员为public）
  }
  ```

- this指针

  - 用途
    - 形参和成员变量同名时，可用this指针区分（不过按照编码规范，成员变量后一般会加`_`，以区分成员变量和其他变量）
    - 区分不同对象的类成员
    - 如果在非静态成员返回对象本身时，可用`return *this`

  - 例子1：形参和成员变量同名情况

    ```c++
    class Person{
    public:
        Person(int age){
            this->age = age;  //形参和成员变量同名
        }
        int age;
    };
    ```

  - 例子2：区分不同对象的类成员，并返回对象本身

    ```c++
    class Person{
    public:
        Person(int age): age_(age){};
        Person& AddAge(Person &p){
            this->age_ += p->age_; //区分不同对象的类成员
            return *this;          //返回对象本身就可以做到无限追加
        }
        int age_;
    };
    int main(){
        Person p1(10);
        Person p2(10);
        p2.AddAge(p1).AddAge(p1).AddAge(p1);  //此时p2->age为40
    }
    ```

    

- const修饰成员函数和对象、mutable关键字

  - 作用：

    - const修饰成员函数（常函数）时，成员函数的this指向就不可修改，**同时指向的值也不能修改**
    - const修饰对象（常对象）时，成员变量不能修改，除非被mutable关键字修饰，同时只能调用常函数
    - 使用mutable修饰成员变量可解除const修饰的限制

  - 例子：

    ```c++
    class Person{
    public:
        void ShowPerson() const{  //定义常函数
            //this->a_ = 100;  //错误，常函数的this指针的指向和指向的值都不能修改
            this->b_ = 100;    //正确，b被mutable关键字修饰
            std::cout << this->b << std::endl;
        }
        int a_;
        mutable int b;
    };
    int main(){
        const Person p;  //常对象
        //p.a_ = 100;    //错误，常函数的this指针的指向和指向的值都不能修改
        p.b_ = 100;      //正确，b被mutable关键字修饰
        p.ShowPerson();  //只能调用常函数
    }
    ```

    

## 模板

### 函数模板

- 作用：建立一个通用函数，返回值和形参可以不确定，用虚拟的类型来表示

- 语法：
	```c++
	// 函数模板声明
	template<typename T>
	void Swap(T &a_, T &b_){
	    T temp_ = a_;
	    a_ = b;
	    b_ = temp_;
	}
	
	// 函数模板的使用(两种方式)
	int test(){
	    int a = 10;
	    int b = 20;
	    // 方法1. 自动类型推导
	    Swap(a, b); 
	    // 方法2：显示指定的类型 （*更好，显式指定了模板参数，可以避免一些潜在的模板推导问题）
	    Swap<int>(a, b);
	}
	```

​	template --- 声明要创建模板了

​	typename --- 表示后面的符号是一种数据类型，可以用class代替

- 注意要点
  - 自动类型推导，必须推导出一致的类型才能使用
  - 模板必须确定 T 的数据类型

- 具体化模板

  - 模板并不是万能的，自己定义的类传入后，可能无法实现正常的功能

  - 使用具体化模板，可以使模板变得更加通用

    ```c++
    // 定义一个正常的模板
    template <class T>
    void compare(T &a, T &b){
        if(a > b){
            std::cout << "a big." << std::endl;
        }else{
            std::cout << "b big." << std::endl;
        }
    }
    
    // 具体化前面的模板
    template <>
    void compare(Person &p1, Person &p2){
        if(p1.age > p2.age){
            std::cout << "p1 big." << std::endl;
        }else{
            std::cout << "p2 big." << std::endl;
        }
    }
    
    // 定义了一个Person类
    class Person{
    public:
        Person(string name, int age): name_(name), age_(age){}
        
    	string name_;
        int age_;
    };
    
    int main(){
        Person a("小明", 20);
        Person b("小张", 24);
        compare(a, b);
        //或者下面这个更好
        compare<Person>(a, b);
    }
    ```

    

### 类模板

- 语法

  ```c++
  // 定义一个类模板
  template <class NameType, class AgeType>
  class Person
  {
  public:
      Perosn(NameType name, AgeType age){
          name_ = name;
          age_ = age;
      }
      NameType name_;
      AgeType age_;
  };
  // 用类模板创建一个类
  void test（）{
      Person<string int> p1("小明"， 18);
  }
  ```

- 与函数模板的区别

  - 类模板没有自动类型推导
  - 类模板在模板的参数列表中可以有**默认参数**

  ```c++
  template <class NameType, class AgeType = int>  // 设置默认参数
  class Person
  {
  public:
      Perosn(NameType name, AgeType age){
          name_ = name;
          age_ = age;
      }
      NameType name_;
      AgeType age_;
  };
  void test（）{
      Person<string> p1("小明"， 18);  // 设置了默认参数，可以不传入该类型
  }
  ```

- 类模板的成员函数并不是一开始就创建的，而是在调用的时候才创建的

- 类模板对象作为函数的参数

  - 方法1：指定传入类型（最常用）
  - 方法2：参数模板化
  - 方法3：整个类模板化

  ```c++
  template<class T1, class T2>
  class Person{
  public:
      Person(T1 name, T2 age){
          name_ = name;
          age_ = age;
      }
      T1 name_;
      T2 age_;
      void print_msg(){
          std::cout << "name:" << this->name_ << "age:" << this->age_ << std::endl;
      }
  };
  
  // 1. 指定传入类型
  void test01(Person<string, int>&p1){
      p1.print_msg();
  }
  
  // 2.参数模板化
  template<class T1, class T2>
  void test02(Person<T1, T2>&p2){
      p2.print_msg();
  }
  
  // 3.整个类模板化
  template<class T>
  void test03(T &p3){
      p3.print_msg();
  }
      
  void test00(){
      Person<string, int>p0("小明", 18);  // 实例化类模板对象
      test01(p0);  // 实例化对象传入函数
      test02(p0);
      test03(p0);
  }
  
  ```

  

- 类模板与继承

  - 继承父类时，如果子类是类模板，不用指定父类的 T 的类型

  - 继承父类时，如果子类不是类模板，需要指定父类的 T 的类型

    ```c++
    template<class T>
    class Base{
    public:
        T a_;
    };
    
    // 子类是类模板，不用指定父类的 T 的类型
    template<class T1, class T2>
    class demo02: public Base<T2>{
    public:
        T1 b_;
    };
    
    // 子类不是类模板，需要指定父类的 T 的类型
    class demo01: public Base<int>{
    };
    
    void test01(){
        demo01 S1;
        demo02<int, char> S2; // 此时 S2 的父类模板的 T 为 char， 子类模板的 T1 为 int
    }
    ```

    

- 类模板成员函数在类外实现

  ```c++
  ```

  
