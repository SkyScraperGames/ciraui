<template>
  <div>
    <div class="container" v-html="lesson"></div>
    <editor :code="code"></editor>
  </div>
</template>

<script>
  import Editor from '../partials/Editor';

  export default {
    props: ['game'],
    data() {
      return {
        code: '',
        lesson: '',
      };
    },
    components: {
      Editor,
    },
    watch: {
      /* eslint-disable */
      '$route.params.lesson': function (lesson) {
        this.loadLesson(lesson);
      },
    },
    mounted() {
      this.loadLesson(this.$route.params.lesson);
    },
    methods: {
      loadLesson(lesson) {
        import(`../../assets/lessons/${lesson}/code.py`)
          .then((file) => {
            this.code = file;
          });
        import(`../../assets/lessons/${lesson}/lesson.html`)
          .then((file) => {
            this.lesson = file;
          });
      },
    },
  };
</script>
