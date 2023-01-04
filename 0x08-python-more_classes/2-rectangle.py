<pre><font color="#C4A000"><b> 14 </b></font><font color="#75507B"><b>        &quot;&quot;&quot;</b></font>
<font color="#C4A000"><b> 15 </b></font>        self.width = width
<font color="#C4A000"><b> 16 </b></font>        self.height = height
<font color="#C4A000"><b> 17 </b></font>
<font color="#C4A000"><b> 18 </b></font>    <font color="#3465A4"><b>@</b></font><font color="#06989A"><b>property</b></font>
<font color="#C4A000"><b> 19 </b></font>    <font color="#C4A000"><b>def</b></font> <font color="#06989A"><b>width</b></font>(self):
<font color="#C4A000"><b> 20 </b></font>        <font color="#75507B"><b>&quot;&quot;&quot;Get/set the width of the Rectangle.&quot;&quot;&quot;</b></font>
<font color="#C4A000"><b> 21 </b></font>        <font color="#C4A000"><b>return</b></font> self.__width
<font color="#C4A000"><b> 22 </b></font>
<font color="#C4A000"><b> 23 </b></font>    <font color="#3465A4"><b>@</b></font><font color="#06989A"><b>width.setter</b></font>
<font color="#C4A000"><b> 24 </b></font>    <font color="#C4A000"><b>def</b></font> <font color="#06989A"><b>width</b></font>(self, value):
<font color="#C4A000"><b> 25 </b></font>        <font color="#C4A000"><b>if</b></font> <font color="#C4A000"><b>not</b></font> <font color="#06989A"><b>isinstance</b></font>(value, <font color="#06989A"><b>int</b></font>):
<font color="#C4A000"><b> 26 </b></font>            <font color="#C4A000"><b>raise</b></font> <font color="#4E9A06"><b>TypeError</b></font>(<font color="#75507B"><b>&quot;width must be an integer&quot;</b></font>)
<font color="#C4A000"><b> 27 </b></font>        <font color="#C4A000"><b>if</b></font> value &lt; <font color="#75507B"><b>0</b></font>:
<font color="#C4A000"><b> 28 </b></font>            <font color="#C4A000"><b>raise</b></font> <font color="#4E9A06"><b>ValueError</b></font>(<font color="#75507B"><b>&quot;width must be &gt;= 0&quot;</b></font>)
<font color="#C4A000"><b> 29 </b></font>        self.__width = value
<font color="#C4A000"><b> 30 </b></font>
<font color="#C4A000"><b> 31 </b></font>    <font color="#3465A4"><b>@</b></font><font color="#06989A"><b>property</b></font>
<font color="#C4A000"><b> 32 </b></font>    <font color="#C4A000"><b>def</b></font> <font color="#06989A"><b>height</b></font>(self):
<font color="#C4A000"><b> 33 </b></font>        <font color="#75507B"><b>&quot;&quot;&quot;Get/set the height of the Rectangle.&quot;&quot;&quot;</b></font>
<font color="#C4A000"><b> 34 </b></font>        <font color="#C4A000"><b>return</b></font> self.__height
<font color="#C4A000"><b> 35 </b></font>
<font color="#C4A000"><b> 36 </b></font>    <font color="#3465A4"><b>@</b></font><font color="#06989A"><b>height.setter</b></font>
<font color="#C4A000"><b> 37 </b></font>    <font color="#C4A000"><b>def</b></font> <font color="#06989A"><b>height</b></font>(self, value):
<font color="#C4A000"><b> 38 </b></font>        <font color="#C4A000"><b>if</b></font> <font color="#C4A000"><b>not</b></font> <font color="#06989A"><b>isinstance</b></font>(value, <font color="#06989A"><b>int</b></font>):
<font color="#C4A000"><b> 39 </b></font>            <font color="#C4A000"><b>raise</b></font> <font color="#4E9A06"><b>TypeError</b></font>(<font color="#75507B"><b>&quot;height must be an integer&quot;</b></font>)
<font color="#C4A000"><b> 40 </b></font>        <font color="#C4A000"><b>if</b></font> value &lt; <font color="#75507B"><b>0</b></font>:
<font color="#C4A000"><b> 41 </b></font>            <font color="#C4A000"><b>raise</b></font> <font color="#4E9A06"><b>ValueError</b></font>(<font color="#75507B"><b>&quot;height must be &gt;= 0&quot;</b></font>)
<font color="#C4A000"><b> 42 </b></font>        self.__height = value
<font color="#C4A000"><b> 43 </b></font>
<font color="#C4A000"><b> 44 </b></font>    <font color="#C4A000"><b>def</b></font> <font color="#06989A"><b>area</b></font>(self):
<font color="#C4A000"><b> 45 </b></font>        <font color="#75507B"><b>&quot;&quot;&quot;Return the area of the Rectangle.&quot;&quot;&quot;</b></font>
<font color="#C4A000"><b> 46 </b></font>        <font color="#C4A000"><b>return</b></font> (self.__width * self.__height)
<font color="#C4A000"><b> 47 </b></font>
<font color="#C4A000"><b> 48 </b></font>    <font color="#C4A000"><b>def</b></font> <font color="#06989A"><b>perimeter</b></font>(self):
<font color="#C4A000"><b> 49 </b></font>        <font color="#75507B"><b>&quot;&quot;&quot;Return the perimeter of the Rectangle.&quot;&quot;&quot;</b></font>
<font color="#C4A000"><b> 50 </b></font>        <font color="#C4A000"><b>if</b></font> self.__width == <font color="#75507B"><b>0</b></font> <font color="#C4A000"><b>or</b></font> self.__height == <font color="#75507B"><b>0</b></font>:
<font color="#C4A000"><b> 51 </b></font>            <font color="#C4A000"><b>return</b></font> (<font color="#75507B"><b>0</b></font>)
<font color="#C4A000"><b> 52 </b></font>        <font color="#C4A000"><b>return</b></font> ((self.__width * <font color="#75507B"><b>2</b></font>) + (self.__height * <font color="#75507B"><b>2</b></font>))
<font color="#C4A000"><b> 53 </b></font>
<font color="#C4A000"><b> 54 </b></font>    <font color="#C4A000"><b>def</b></font> <font color="#06989A"><b>__str__</b></font>(self):
<font color="#C4A000"><b> 55 </b></font>        <font color="#75507B"><b>&quot;&quot;&quot;Return the printable representation of the Rectangle.</b></font>
<font color="#C4A000"><b> 56 </b></font>
<font color="#C4A000"><b> 57 </b></font><font color="#75507B"><b>        Represents the rectangle with the # character.</b></font>
<font color="#C4A000"><b> 58 </b></font><font color="#75507B"><b>        &quot;&quot;&quot;</b></font>
<font color="#C4A000"><b> 59 </b></font>        <font color="#C4A000"><b>if</b></font> self.__width == <font color="#75507B"><b>0</b></font> <font color="#C4A000"><b>or</b></font> self.__height == <font color="#75507B"><b>0</b></font>:
<font color="#C4A000"><b> 60 </b></font>            <font color="#C4A000"><b>return</b></font> (<font color="#75507B"><b>&quot;&quot;</b></font>)
<font color="#C4A000"><b> 61 </b></font>
<font color="#C4A000"><b> 62 </b></font>        rect = []
<font color="#C4A000"><b> 63 </b></font>        <font color="#C4A000"><b>for</b></font> i <font color="#C4A000"><b>in</b></font> <font color="#06989A"><b>range</b></font>(self.__height):
<font color="#C4A000"><b> 64 </b></font>            [rect.append(<font color="#75507B"><b>&apos;#&apos;</b></font>) <font color="#C4A000"><b>for</b></font> j <font color="#C4A000"><b>in</b></font> <font color="#06989A"><b>range</b></font>(self.__width)]
<font color="#C4A000"><b> 65 </b></font>            <font color="#C4A000"><b>if</b></font> i != self.__height - <font color="#75507B"><b>1</b></font>:
<font color="#C4A000"><b> 66 </b></font>                rect.append(<font color="#75507B"><b>&quot;</b></font><font color="#CC0000"><b>\n</b></font><font color="#75507B"><b>&quot;</b></font>)
<font color="#C4A000"><b> 67 </b></font>        <font color="#C4A000"><b>return</b></font> (<font color="#75507B"><b>&quot;&quot;</b></font>.join(rect))
</pre>#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if sel)
