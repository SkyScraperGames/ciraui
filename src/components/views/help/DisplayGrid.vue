<template>
  <div class="container content">
    <h1>Display Grid</h1>

    <img src="../../../assets/DotsArrow.png" alt="CiraEmulatorDisplay" width="183" height="224">

    <p>To place pixels on the Cira Center display, our program uses a grid. This grid uses an x value, to describe where the pixel
      will be placed along the width of the display, from left to right.</p>

    <img src="../../../assets/DotsHorizontalArrow.png" alt="CiraEmulatorDisplayWidth" width="183" height="224">

    <p>If the x value is 0, the pixel will be placed on left side of the screen.</p>
    <p>If the x value is 19, it will be placed on the right side. The x value can be any whole number between 0 and 19.</p>

    <p>The grid also has a y value, which describes where along the length of the display the pixel will be placed.</p>

    <img src="../../../assets/DotsVerticalArrow.png" alt="CiraEmulatorDisplayHeight" width="183" height="224">

    <p>If the y value is 0, the pixel will be placed on the top. If the y value is 22, the pixel will be placed on the bottom.</p>

    <p></p>So, to put a pixel in the top left corner, it would have an x value of 0 and a y value of 0.
    <p>
      <br>
    </p>
    <h4>Here are some Python functions that relate to parts of the display grid:</h4>
    <pre><code>clearPoint(x, y)</code></pre>
    <pre><code>putPixel(x, y, r, g, b)</code></pre>
    <pre><code>getHeight()</code></pre>
    <pre><code>getWidth()</code></pre>
    <pre><code>isYin(y)</code></pre>
    <pre><code>isXin(x)</code></pre>
  </div>
</template>
