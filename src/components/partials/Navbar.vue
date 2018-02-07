<template>
  <nav class="navbar is-transparent" :class="{ 'is-black': !isHome, 'open': open }" v-on-clickaway="close" role="navigation" aria-label="main navigation">
    <div class="container">
      <div class="navbar-brand">
        <router-link class="navbar-item" to="/" @click.native="close">
          <img class="navbar-brand-logo" src="../../assets/logo.png" alt="Skyscraper Games Logo">
          <span class="navbar-brand-text">Skyscraper Games</span>
        </router-link>

        <button class="button navbar-burger" @click="toggleOpen">
          <span></span>
          <span></span>
          <span></span>
        </button>
      </div>

      <div class="navbar-end">
        <router-link class="navbar-item" to="/editor" @click.native="close">
          Editor
        </router-link>
        <router-link class="navbar-item" to="/help" @click.native="close">
          Help
        </router-link>
        <b-dropdown position="is-bottom-left">
          <a class="navbar-item" slot="trigger">
            <span>Lessons</span>
            <b-icon class="is-hidden-touch" icon="menu-down"></b-icon>
          </a>

          <b-dropdown-item has-link>
            <router-link to="/lessons/1">Lesson 1</router-link>
          </b-dropdown-item>
          <b-dropdown-item has-link>
            <router-link to="/lessons/2">Lesson 2</router-link>
          </b-dropdown-item>
          <b-dropdown-item has-link>
            <router-link to="/lessons/3">Lesson 3</router-link>
          </b-dropdown-item>
          <b-dropdown-item has-link>
            <router-link to="/lessons/4">Lesson 4</router-link>
          </b-dropdown-item>
          <b-dropdown-item has-link>
            <router-link to="/lessons/5">Lesson 5</router-link>
          </b-dropdown-item>
          <b-dropdown-item has-link>
            <router-link to="/lessons/6">Lesson 6</router-link>
          </b-dropdown-item>
          <b-dropdown-item has-link>
            <router-link to="/lessons/7">Lesson 7</router-link>
          </b-dropdown-item>
          <b-dropdown-item has-link>
            <router-link to="/lessons/8">Lesson 8</router-link>
          </b-dropdown-item>
        </b-dropdown>
        <b-dropdown position="is-bottom-left">
          <a class="navbar-item" slot="trigger">
            <span>Games</span>
            <b-icon class="is-hidden-touch" icon="menu-down"></b-icon>
          </a>

          <b-dropdown-item has-link>
            <router-link to="/game/flappydot">Flappy Bird</router-link>
          </b-dropdown-item>
          <b-dropdown-item has-link>
            <router-link to="/game/skyscraperSnake">Skyscraper Snake</router-link>
          </b-dropdown-item>
          <b-dropdown-item has-link>
            <router-link to="/game/superTetragon">Super Tetragon</router-link>
          </b-dropdown-item>
          <b-dropdown-item has-link>
            <router-link to="/game/mazeShakalaka">Maze Shaka-Laka</router-link>
          </b-dropdown-item>
        </b-dropdown>
        <b-dropdown position="is-bottom-left" v-if="!user">
          <div class="navbar-item" slot="trigger">
            <p class="control has-text-centered">
              <a class="button is-primary">
                <span>Log in</span>
              </a>
            </p>
          </div>

          <b-dropdown-item custom paddingless ref="loginDropdown">
            <form @submit.prevent="submit">
              <div class="modal-card" style="width:300px;">
                <section class="modal-card-body">
                  <b-notification v-if="formError" type="is-danger" has-icon>
                    {{ formError }}
                  </b-notification>
                  <b-field label="Email">
                    <b-input
                      type="email"
                      placeholder="Email"
                      required
                      v-model="email">
                    </b-input>
                  </b-field>

                  <b-field label="Password">
                    <b-input
                      type="password"
                      password-reveal
                      placeholder="Password"
                      required
                      v-model="password">
                    </b-input>
                  </b-field>

                  <b-checkbox v-model="remember">Remember me</b-checkbox>
                  <div>
                    <button class="button is-primary mt-20" :class="{ 'is-loading': buttonLoading }">Login</button>
                  </div>
                  <div class="mt-20">
                    <router-link @click.native="closeLoginDropdown" to="/user/register">Don't have an account? Sign up!</router-link>
                  </div>
                </section>
              </div>
            </form>
          </b-dropdown-item>
        </b-dropdown>
        <b-dropdown position="is-bottom-left" v-else>
          <a class="navbar-item" slot="trigger">
            <span>{{ user }}</span>
            <b-icon class="is-hidden-touch" icon="menu-down"></b-icon>
          </a>

          <b-dropdown-item has-link>
            <router-link to="/user/profile">Profile</router-link>
          </b-dropdown-item>
          <b-dropdown-item @click="logout">Log out</b-dropdown-item>
        </b-dropdown>
      </div>
    </div>
  </nav>
</template>

<script>
  import { mixin as clickaway } from 'vue-clickaway';
  import { mapState, mapActions } from 'vuex';

  import { login } from '../../api/user';

  export default {
    mixins: [clickaway],
    data() {
      return {
        open: false,
        email: '',
        password: '',
        remember: false,
        buttonLoading: false,
        formError: null,
      };
    },
    computed: {
      isHome() {
        return this.$route.path === '/';
      },
      ...mapState([
        'user',
      ]),
    },
    methods: {
      ...mapActions([
        'login',
        'logout',
      ]),
      toggleOpen() {
        this.open = !this.open;
      },
      close() {
        this.open = false;
      },
      submit() {
        this.buttonLoading = true;
        this.formError = null;

        const vm = this;

        login(this.email, this.password, this.remember)
          .then((response) => {
            if (!response.ok) {
              response.json().then((data) => {
                vm.formError = data.message;
              });
              return;
            }

            this.login(this.email);
            this.$router.push('/user/profile');
          })
          .catch(() => {
            this.formError = 'An unknown error occured. Please try again.';
          })
          .finally(() => {
            this.buttonLoading = false;
          });
      },
      closeLoginDropdown() {
        // TODO Implement once fix hits NPM https://github.com/rafaelpimpa/buefy/issues/543
      },
    },
  };
</script>


<style lang="scss" scoped>
  @import "../../styles/_variables";

  .navbar {
    height: 80px;
    transition: background 0.2s ease-in-out;
    position: relative;
    z-index: 10;
  }

  .is-transparent {
    background: transparent;
    margin-bottom: -$navbar-height;

    a.navbar-item:hover {
      color: #FFF;
      background-color: transparent;
    }
  }

  .is-black {
    margin-bottom: 20px;
  }

  .navbar-burger {
    background: transparent;
    border: none;

    span {
      background-color: #FFF;
    }
  }

  .navbar-brand-logo {
    margin-right: 20px;
  }

  .navbar-brand-text {
    font-size: 1.2em;
    font-weight: 500;
    text-transform: uppercase;
  }

  .navbar-item {
    color: #FFF;
  }

  @media screen and (max-width: 1025px) {
    .navbar.open {
      background-color: #0a0a0a;

      .navbar-end {
        max-height: 1000px;
      }
    }

    .navbar-end {
      background: #333;
      max-height: 0;
      transition: max-height 0.3s ease-in-out;
      overflow: hidden;

      .dropdown {
        display: block;
        flex-grow: 0;
        flex-shrink: 0;
      }

      .navbar-item {
        text-align: center;
        padding-top: 15px;
        padding-bottom: 15px;
      }
    }
  }

  .dropdown-item .icon, .has-link .icon {
    vertical-align: middle;
  }

  .dropdown-text {
    vertical-align: middle;
  }

  .navbar .dropdown + .dropdown {
    margin: 0;
  }
</style>
