<template>
  <div>
    <div class="container">
      <article class="message is-primary mb-25">
        <div class="message-body">
          <h2 class="is-size-3">Pixel Calculator</h2>
          We are going to find out the total number of lights on the Cira Centre using 'variables.' Pretend you are
          moving and have to pack up everything you own. You want to be able to find your clothes when you unpack. You
          label the outside of a box, 'clothing' and put your clothing inside of it. This makes it easier to find your
          clothing when you need it. In this case 'clothing' is like a variable. The clothing inside of the box is the
          data you want to store. Variables are like boxes. They store data and make it easy to find that data when you
          need it.
          <article class="message is-warning mt-20">
            <div class="message-header">
              <p><b>For you to do</b></p>
            </div>
            <div class="message-body">
              In this lesson you will learn how to make three variables and use them to figure out the total number of
              lights on the Centre.
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
      import('../../../assets/python/lessons/lesson3.py')
        .then((file) => {
          this.code = file;
          this.name = 'lesson3.py';
        });
    },
  };
</script>
