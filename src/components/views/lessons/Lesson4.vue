<template>
  <div>
    <div class="container">
      <article class="message is-primary mb-25">
        <div class="message-body">
          <h2 class="is-size-3">Drawing a Pixel</h2>
          putPixel is a function that gives the pixel a location and a color. The putPixel function uses x and y for the location.
          <hr>
          Here is an example of the putPixel function.
          <pre>cira.display.putPixel(x, y, r, g, b)</pre>
          <hr>
          To place pixels on the Cira Center display, our program uses a grid. That grid uses the x, y values in the putPixel function to describe the pixel’s location.
          The x value describes where the pixel will be placed along the width of the display, from left to right. The y value describes where along the length of the display the pixel will be placed, from top to bottom.

          <article class="message is-warning mt-20">
            <div class="message-header">
              <p><b>For you to do</b></p>
            </div>
            <div class="message-body">
              Try moving the pixel to the top right corner!
            </div>
          </article>
        </div>
      </article>
    </div>
    <editor :code="code"></editor>
  </div>
</template>

<script>
  import Editor from '../../partials/Editor';

  export default {
    props: ['game'],
    data() {
      return {
        code: '',
      };
    },
    components: {
      Editor,
    },
    mounted() {
      import('../../../assets/python/lessons/lesson4.py')
          .then((file) => { this.code = file; });
    },
  };
</script>
