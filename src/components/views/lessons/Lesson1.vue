<template>
  <div>
    <div class="container">
      <article class="message is-primary mb-25">
        <div class="message-body">
          <h2 class="is-size-3">Commenting</h2>
          Comments are bits of code that can help you learn what the code is doing. Comments do not get read by
          computers. Comments always begin with a "#"!
          <article class="message is-warning mt-20">
            <div class="message-header">
              <p><b>For you to do</b></p>
            </div>
            <div class="message-body">
              Write your own comment in the editor. Be sure to start with a #!
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
      import('../../../assets/python/lessons/lesson1.py')
        .then((file) => {
          this.code = file;
          this.name = 'lesson1.py';
        });
    },
  };
</script>
