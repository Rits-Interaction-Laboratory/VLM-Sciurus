import rospy
from std_msgs.msg import String

def prom_publisher():
    # 初始化 ROS 节点
    rospy.init_node('prom_publisher2', anonymous=True)
    
    # 创建一个 Publisher，话题名称为 'prom_topic'，消息类型为 String
    pub = rospy.Publisher('prom_topic', String, queue_size=10)
    
    # 定义要发布的文字
    prom_text = """
    aaaaaaaaaaaaaaaaaaaaa
    bbbbbbbbbbbbbbbbbbbbbbb
    cccccccccccccccccccccc
    ddddddddddddddddd
    eeeeeeeeeeeeee
    fffffffffff
    ggggggggggggggg
    hhhhhhhhhhhhhhhhhhhh
    iiiiiiiiiiiiii
    gggggggggggggggggggggg
    kkkkkkkkkkkkkkkkkkkkkk
    llllllllllllllllllll
    mmmmmmmmmmmmmmmmm
    nnnnnnnnnnnnnnnnnnnn
    oooooooooooooo
    pppppppppp
    qqqqqqqqqqq
    rrrrrrrrrrrrr
    ssssssssssssss
    tttttttttttttttttt
    uuuuuuuuuuuuuuuuuuuuuuu
    vvvvvvvvvvvvvvvvvvv
    wwwwwwwwwwwwwwww
    xxxxxxxxxxxxxx
    yyyyyyyyyyyyyyyyy
    zzzzzzzzzzzzzz
    """

    while not rospy.is_shutdown():
        # 等待用户输入
        user_input = input("请输入 '1' 来发布 prom_text，或按 'q' 退出: ")
        print(prom_text)
        if user_input == "1":
            rospy.loginfo("Publishing prom text")
            pub.publish(prom_text)
        elif user_input == "q":
            break

if __name__ == '__main__':
    try:
        prom_publisher()
    except rospy.ROSInterruptException:
        pass

