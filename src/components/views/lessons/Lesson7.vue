<template>
  <div>
    <div class="container">
      <article class="message is-primary mb-25">
        <div class="message-body">
          <h2 class="is-size-3">Using Variables</h2>
          Variables are like boxes – they are good places to store things and recall them later. Add items to the
          variables ‘fruit’ and ‘veggies’ and see what happens when you add those variables together!
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
      import('../../../assets/python/lessons/lesson7.py')
        .then((file) => {
          this.code = file;
          this.name = 'lesson7.py';
        });
    },
  };
</script>
