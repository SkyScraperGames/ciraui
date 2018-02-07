<template>
  <div>
    <div class="container">
      <article class="message is-primary mb-25">
        <div class="message-body">
          <h2 class="is-size-3">Hello World</h2>
          'Print' prints out text and numbers in the output box. Print functions are always followed by text or numbers
          in single quotes.
          <article class="message is-warning mt-20">
            <div class="message-header">
              <p><b>For you to do</b></p>
            </div>
            <div class="message-body">
              Use the 'print' command to write 'Hello, World!' in the output box. The words or numbers you would like to
              print should be in quotes.
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
      import('../../../assets/python/lessons/lesson2.py')
        .then((file) => {
          this.code = file;
          this.name = 'lesson2.py';
        });
    },
  };
</script>
