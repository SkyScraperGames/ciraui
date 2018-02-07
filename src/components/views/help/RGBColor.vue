<template>
  <div class="container content">
    <h1>RGB Color</h1>

    <p> For computers, the color of a single pixel is set using “RGB Values.” Here, RGB is an acronym for Red, Green, and Blue.
      This means that any color can be made by combing different amounts of red, green, and blue. To make a color, you will
      need to give&nbsp;a number to the R, G, and B variables. These numbers can be anything from 0 to 255, where 0 is none
      of that color, and 255 is the most. In this case, higher numbers make brighter colors and lower numbers make darker ones.
      </p>
    <br>
    <h4>For example:</h4>

    <p>– (255, 0, 0) is completely red, as it has the highest possible value for R, and no G or B</p>
    <p>– (255, 0, 255) would be&nbsp;the most purple color possible, since you are blending the maximum amounts of R and&nbsp;B,
      and using no G.</p>
    <br>

    <h4>Here is a diagram showing some RGB color combinations:</h4>

    <img src="../../../assets/RGB-Examples-1-300x186.jpg" alt="RGB Examples" width="300" height="186">

    <h4>Here are some Python functions that involve the use of RGB color:</h4>
    <pre><code>clearScreen(r, g, b)</code></pre>
    <pre><code>putPixel(x, y, r, g, b)</code></pre>
  </div>
</template>
