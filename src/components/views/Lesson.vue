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
      '$route.params.lessonGroup': function (lessonGroup) {
        this.loadLesson(lessonGroup, this.$route.params.lesson);
      },
      '$route.params.lesson': function (lesson) {
        this.loadLesson(this.$route.params.lessonGroup, lesson);
      },
    },
    mounted() {
      this.loadLesson(this.$route.params.lessonGroup, this.$route.params.lesson);
    },
    methods: {
      loadLesson(lessonGroup, lesson) {
        import(`../../assets/lessons/${lessonGroup}/${lesson}/code.py`)
          .then((file) => {
            this.code = file;
          });
        import(`../../assets/lessons/${lessonGroup}/${lesson}/lesson.html`)
          .then((file) => {
            this.lesson = file;
          });
      },
    },
  };
</script>
