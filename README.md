# UIPOFramework
UI自动化测试框架-PO模式

工程结构说明：

整个测试框架分为四层，通过分层的方式，测试代码更容易理解，维护起来较为方便。

第一层是基础测试库：

* util 包：用于实现测试过程中调用的工具类方法，例如读取配置文件、页面元素的操作方法、操作Excel文件等。
* conf 包：配置文件及全局变量。
* test_data 目录：Excel 数据文件，包含测试数据输入、测试结果输出。
* log 目录：日志输出文件。
* screenshot_path 目录：异常截图保存目录。

第二层是服务层，相当于对测试对象的一个业务封装。对于接口测试，是对远程方法的一个实现；对于页面测试，是对页面元素或操作的一个封装。
* page 包：对象库层及操作层，将所有页面的元素对象定位及其操作分别封装成一个类。

第三层测试用例逻辑层，该层主要是将服务层封装好的各个业务对象，组织成测试逻辑，进行校验。
* action 包：业务层，将一个或多个操作组合起来完成一个业务功能。

第四层测试场景，将测试用例组织成测试场景，实现各种级别 cases 的管理、冒烟，回归等测试场景。
* test_script 包：基于业务层和测试文件，实现数据驱动的测试执行脚本。
* test_data 目录：Excel 数据文件，包含测试数据输入、测试结果输出。　　
* run_test.py：本 PO 框架的运行主入口。

<br></br>
框架特点：
1. 通过配置文件，实现页面元素定位方式和测试代码的分离。
2. 使用 PO 模式，封装了网页中的页面元素，方便测试代码调用，也实现了一处维护全局生效的目标。
3. 在 excel 文件中定义多组测试数据，每个登录用户都一一对应一个存放联系人数据的 sheet，测试框架可自动调用测试数据完成数据驱动测试。
4. 实现了测试执行过程中的日志记录功能，可以通过日志文件分析测试脚本执行的情况。
5. 在 excel 数据文件中，通过设定“测试数据是否执行”列的内容为 y 或 n，自定义选择测试数据，测试执行结束后会在"测试结果列"中显示测试执行的时间和结果，方便测试人员查看。
