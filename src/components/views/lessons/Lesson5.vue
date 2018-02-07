<template>
  <div>
    <div class="container">
      <article class="message is-primary mb-25">
        <div class="message-body">
          <h2 class="is-size-3">Drawing a Picture</h2>
          The <tt>putPixel</tt> function can be typed many times to make a picture.
          <pre>cira.display.putPixel(10, 10, 0, 255, 0)</pre>
          <pre>cira.display.putPixel(11, 10, 0, 255, 0) </pre>
          <pre>cira.display.putPixel(12, 10, 0, 255, 0) </pre>
          The 3 <tt>putPixel</tt> functions above make a green line that is 3 pixels wide.

          <article class="message is-warning mt-20">
            <div class="message-header">
              <p><b>For you to do</b></p>
            </div>
            <div class="message-body">
              Use the putPixel function to draw a character from your Game Design Document.
              You will need a putPixel function for each pixel in your character.
              If your character is made of 5 pixels then you will need 5 putPixel functions. Don’t use more than 8
              pixels!
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
      import('../../../assets/python/lessons/lesson5.py')
        .then((file) => {
          this.code = file;
          this.name = 'lesson5.py';
        });
    },
  };
</script>
