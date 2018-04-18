<template>
<form class="container login-form" @submit.prevent="submit">
  <b-notification v-if="formError" type="is-danger" has-icon>
    {{ formError }}
  </b-notification>
  <h1 class="is-size-1 mb-25 mt-25">Change Recovery Email</h1>

  <b-field label="Current Password">
    <b-input
      type="password"
      password-reveal
      placeholder="Current Password"
      required
      v-model="oldPassword">
    </b-input>
  </b-field>

  <b-field label="New Recovery Email">
    <b-input
      type="email"
      placeholder="New Recovery Email"
      required
      v-model="newRecoveryEmail">
    </b-input>
  </b-field>

  <div>
    <button class="button is-primary mt-20" :class="{ 'is-loading': buttonLoading }">Change Recovery Email</button>
  </div>
</form>
</template>

<script>
  import { changeEmail } from '../../../api/user';

  export default {
    data() {
      return {
        oldPassword: '',
        newRecoveryEmail: '',
        buttonLoading: false,
        formError: null,
      };
    },
    methods: {
      submit() {
        this.buttonLoading = true;
        this.formError = null;

        const vm = this;

        changeEmail(this.newRecoveryEmail, this.oldPassword)
          .then((response) => {
            if (!response.ok) {
              response.json().then((data) => {
                vm.formError = data.message;
              });
              return;
            }

            this.$router.push('/user/profile');
          })
          .catch(() => {
            this.formError = 'An unknown error occured. Please try again.';
          })
          .finally(() => {
            this.buttonLoading = false;
          });
      },
    },
  };
</script>

<style lang="scss" scoped>
  .login-form {
    max-width: 400px;
  }
</style>
