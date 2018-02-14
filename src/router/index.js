import Vue from 'vue';
import Router from 'vue-router';
import store from '../store';

Vue.use(Router);

function view(name) {
  return () => import(`@/components/views/${name}.vue`);
}

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: view('Index'),
    },
    {
      path: '/editor',
      name: 'Editor',
      component: view('Editor'),
    },
    {
      path: '/editor/:id',
      name: 'EditorId',
      component: view('Editor'),
      props: true,
    },
    {
      path: '/editor/games/:game',
      name: 'EditorGame',
      component: view('Editor'),
      props: true,
    },
    {
      path: '/user/login',
      name: 'Login',
      component: view('user/Login'),
    },
    {
      path: '/user/register',
      name: 'Register',
      component: view('user/Register'),
    },
    {
      path: '/user/profile',
      name: 'Profile',
      component: view('user/Profile'),
      meta: { requiresAuth: true },
    },
    {
      path: '/game/:game',
      name: 'Game',
      component: view('Game'),
    },
    {
      path: '/help/booleans',
      name: 'Booleans',
      component: view('help/Booleans'),
    },
    {
      path: '/help/conditionals',
      name: 'Conditionals',
      component: view('help/Conditionals'),
    },
    {
      path: '/help/displayGrid',
      name: 'DisplayGrid',
      component: view('help/DisplayGrid'),
    },
    {
      path: '/help/loops',
      name: 'Loops',
      component: view('help/Loops'),
    },
    {
      path: '/help/pixels',
      name: 'Pixels',
      component: view('help/Pixels'),
    },
    {
      path: '/help/RGBColor',
      name: 'RGBColor',
      component: view('help/RGBColor'),
    },
    {
      path: '/help/whitespace',
      name: 'Whitespace',
      component: view('help/Whitespace'),
    },
    {
      path: '/help',
      name: 'HelpIndex',
      component: view('HelpIndex'),
    },
    {
      path: '/lessons/:lesson',
      name: 'Lesson',
      component: view('Lesson'),
    },
    {
      path: '/lessons',
      name: 'LessonIndex',
      component: view('LessonIndex'),
    },
    {
      path: '/privacy',
      name: 'PrivacyPolicy',
      component: view('PrivacyPolicy'),
    },
  ],
  mode: 'history',
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.state.user && localStorage.getItem('loggedIn') === 'false') {
      next({
        path: '/user/login',
        query: { redirect: to.fullPath },
      });
      return;
    }
  }

  next();
});

export default router;
