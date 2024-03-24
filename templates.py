auth_form = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>403</width>
    <height>434</height>
   </rect>
  </property>
  <property name="cursor">
   <cursorShape>CrossCursor</cursorShape>
  </property>
  <property name="contextMenuPolicy">
   <enum>Qt::DefaultContextMenu</enum>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">#MainWindow{border-image:url(data/Background.png)}</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="btn_enter">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>280</y>
      <width>271</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color:green;
color: white
</string>
    </property>
    <property name="text">
     <string>ВОЙТИ</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>10</y>
      <width>371</width>
      <height>71</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Wide Latin</family>
      <pointsize>26</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: rgb(255, 255, 255)</string>
    </property>
    <property name="text">
     <string>Добро пожаловать!</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>80</y>
      <width>81</width>
      <height>71</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Wide Latin</family>
      <pointsize>16</pointsize>
      <weight>75</weight>
      <italic>true</italic>
      <bold>true</bold>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>ArrowCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">color: rgb(255, 255, 255)</string>
    </property>
    <property name="text">
     <string>Логин</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>140</y>
      <width>101</width>
      <height>71</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Wide Latin</family>
      <pointsize>16</pointsize>
      <weight>75</weight>
      <italic>true</italic>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: rgb(255, 255, 255)</string>
    </property>
    <property name="text">
     <string>Пароль</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="loginEdit">
    <property name="geometry">
     <rect>
      <x>130</x>
      <y>100</y>
      <width>211</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="passwordEdit">
    <property name="geometry">
     <rect>
      <x>130</x>
      <y>150</y>
      <width>211</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="btn_registration">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>340</y>
      <width>271</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color:red;
color: white
</string>
    </property>
    <property name="text">
     <string>РЕГИСТРАЦИЯ</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>190</y>
      <width>361</width>
      <height>101</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Wide Latin</family>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: rgb(255, 255, 255)</string>
    </property>
    <property name="text">
     <string>Профиль с таким логином и паролем не найден</string>
    </property>
    <property name="textFormat">
     <enum>Qt::PlainText</enum>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
    <property name="wordWrap">
     <bool>true</bool>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>403</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""
registration_form = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>521</width>
    <height>447</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">#MainWindow{border-image:url(data/Background.png)}</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>511</width>
      <height>71</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Wide Latin</family>
      <pointsize>18</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color:white</string>
    </property>
    <property name="text">
     <string>Добро пожаловать в окно регистрации!</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>100</x>
      <y>70</y>
      <width>81</width>
      <height>71</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Wide Latin</family>
      <pointsize>16</pointsize>
      <weight>75</weight>
      <italic>true</italic>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: white
</string>
    </property>
    <property name="text">
     <string>Логин</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>130</y>
      <width>101</width>
      <height>71</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Wide Latin</family>
      <pointsize>16</pointsize>
      <weight>75</weight>
      <italic>true</italic>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: white
</string>
    </property>
    <property name="text">
     <string>Пароль</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="loginEdit">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>90</y>
      <width>211</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="passwordEdit">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>140</y>
      <width>211</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="button_reg">
    <property name="geometry">
     <rect>
      <x>120</x>
      <y>260</y>
      <width>281</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color:green;
color: white
</string>
    </property>
    <property name="text">
     <string>ЗАРЕГИСТРИРОВАТЬСЯ</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>120</x>
      <y>200</y>
      <width>271</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Wide Latin</family>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Ваш логин не уникальный</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>521</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""