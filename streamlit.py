import streamlit 
st=streamlit.set_page_config(page_title="nhạc nhẽo",page_icon="fox-logo-01.ico")
col1,col2,col3=streamlit.columns(3)

# with col1:
#     St=streamlit.header("My Penguin")
#     St=streamlit.image("OIP.jpg")
#     St=streamlit.write("Penpen")
#     St=streamlit.write("Full time animal at the international zoo")
# with col3:
#     St=streamlit.write(" ")
#     St=streamlit.write(" ")
#     St=streamlit.write(" ")
#     St=streamlit.write(" ")
#     St=streamlit.write(" ")
#     St=streamlit.write(" ")
    

#     St=streamlit.write("My hobbies:")
#     St=streamlit.write("Hang out full time")
#     St=streamlit.write("Listen to music sometimes")
#     St=streamlit.write("Read books")
#     St=streamlit.write("")
#     St=streamlit.write("[My facebook profile if you interested](https://www.facebook.com/profile.php?id=100028354028197)")

def page1():
    St=streamlit.write(" Đi về nhà - Đen ")
    St=streamlit.video("di ve nha.mp4")
    St=streamlit.write("đi về nhà")
    f=open("di ve nha.mp4","rb")
    st=streamlit.download_button(label="đi về nhà",data=f,file_name="di ve nha.mp4")

def page2():
    St=streamlit.write(" Lối nhỏ - Đen ")
    St=streamlit.video("loi nho.mp4")
    Sr=streamlit.write("lối nhỏ")
    f=open("loi nho.mp4","rb")
    st=streamlit.download_button(label="lối nhỏ",data=f,file_name="loi nho.mp4")

def page3():
    St=streamlit.write(" Ai muốn nghe không? - Đen ")
    St=streamlit.video("ai muon nghe khong.mp4")
    Sr=streamlit.write("ai muốn nghe không?")
    f=open("ai muon nghe khong.mp4","rb")
    st=streamlit.download_button(label="Ai muốn nghe hong",data=f,file_name="ai muon nghe khong.mp4")

page_menu={"Page 1":page1,"Page2":page2,"Page3":page3}
select_page=streamlit.selectbox("select a page",page_menu.keys())
page_menu[select_page]()


    
