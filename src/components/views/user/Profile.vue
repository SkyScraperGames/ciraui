<template>
  <div class="container">
    <h1 class="is-size-3 mb-10">My Profile</h1>
    <form class="container login-form mb-20" @submit.prevent="submit">
      <b-notification v-if="formError" type="is-danger" has-icon>
        {{ formError }}
      </b-notification>

      <b-field label="Gender">
        <b-select placeholder="Select a Gender" v-model="gender">
          <option
            v-for="gender in genders"
            :value="gender"
            :key="gender">
            {{ gender }}
          </option>
        </b-select>
      </b-field>

      <b-field label="Please specify gender" v-if="gender === 'Other'">
          <b-input
            type="text"
            placeholder="Specify gender"
            required
            v-model="genderSpecify">
          </b-input>
      </b-field>

      <div>
        <button class="button is-primary" :class="{ 'is-loading': buttonLoading }">Save</button>
      </div>
    </form>

    <h1 class="is-size-3">My Projects</h1>
    <b-table
      :data="Object.values(files)"
      >

      <template slot-scope="props">
        <b-table-column label="Name">
          <router-link :to="`/editor/${props.row.versions[Object.keys(props.row.versions).length - 1].id}`">{{ props.row.fileName }}</router-link>
        </b-table-column>

        <b-table-column label="Date Created">
          {{ props.row.date }}
        </b-table-column>

        <b-table-column class="has-text-right">
          <button class="button is-primary" @click="openVersionsModal(props.row.fileName)">Versions</button>
          <button class="button is-danger" @click="openDeleteModal(props.row.fileName)">Delete</button>
        </b-table-column>
      </template>
      <template slot="empty">
          <section class="section">
              <div class="content has-text-grey has-text-centered">
                  <p>
                      <b-icon
                          icon="emoticon-sad"
                          size="is-large">
                      </b-icon>
                  </p>
                  <p>Nothing here.</p>
              </div>
          </section>
      </template>
    </b-table>
    <b-modal :active.sync="isVersionsModalActive" v-if="isVersionsModalActive" has-modal-card>
      <div class="modal-card" style="width: auto">
        <header class="modal-card-head">
            <p class="modal-card-title">Versions</p>
        </header>
        <section class="modal-card-body">
          <b-table
            :data="Object.values(files[currentFile].versions)"
            >

            <template slot-scope="props">
              <b-table-column label="#">
                <router-link :to="`/editor/${props.row.id}`">{{ props.row.version }}</router-link>
              </b-table-column>

              <b-table-column label="Date Created">
                {{ props.row.date }}
              </b-table-column>
            </template>
          </b-table>
        </section>
      </div>
    </b-modal>
    <b-modal :active.sync="isDeleteModalActive" has-modal-card>
      <div class="modal-card" style="width: auto">
        <header class="modal-card-head">
            <p class="modal-card-title">Delete File</p>
        </header>
        <section class="modal-card-body">
          Are you sure you want to delete this file?

          <div class="mt-20 has-text-centered">
            <button class="button is-danger" @click="deleteFile(currentFile); isDeleteModalActive = false;">Delete</button>
          </div>
        </section>
      </div>
    </b-modal>
  </div>
</template>

<script>
  import { profile, analytics } from '../../../api/user';
  import { deleteFile } from '../../../api/editor';

  export default {
    data() {
      return {
        files: [],
        isVersionsModalActive: false,
        isDeleteModalActive: false,
        currentFile: null,
        buttonLoading: false,
        formError: null,
        genders: [
          'Female',
          'Male',
          'Prefer not to say',
          'Other',
        ],
        gender: null,
        genderSpecify: null,
      };
    },
    methods: {
      openVersionsModal(name) {
        this.currentFile = name;
        this.isVersionsModalActive = true;
      },
      openDeleteModal(name) {
        this.currentFile = name;
        this.isDeleteModalActive = true;
      },
      deleteFile(name) {
        const vm = this;

        deleteFile(name)
          .then((response) => {
            if (!response.ok) {
              vm.$snackbar.open({
                message: 'An error occured when deleting the file.',
                type: 'is-danger',
              });
              return;
            }

            vm.$delete(vm.files, name);
            vm.$snackbar.open({
              message: 'File deleted!',
              type: 'is-success',
            });
          });
      },
      submit() {
        this.buttonLoading = true;
        this.formError = null;

        const vm = this;

        const gender = this.gender === 'Other' ? this.genderSpecify : this.gender;

        analytics(gender)
          .then((response) => {
            response.json().then((data) => {
              if (!response.ok) {
                vm.formError = data.message;
              }
            });
          })
          .catch(() => {
            this.formError = 'An unknown error occured. Please try again.';
          })
          .finally(() => {
            this.buttonLoading = false;
          });
      },
    },
    mounted() {
      const vm = this;

      profile()
        .then((response) => {
          if (!response.ok) {
            return;
          }

          response.json().then((data) => {
            const finalArray = [];

            data.files.forEach((file) => {
              if (!finalArray[file.fileName]) {
                finalArray[file.fileName] = {};
                finalArray[file.fileName].fileName = file.fileName;
                finalArray[file.fileName].date = file.date;
                finalArray[file.fileName].versions = [];
              }

              finalArray[file.fileName].versions[file.version - 1] = file;
            });

            vm.files = finalArray;

            if (vm.genders.includes(data.gender)) {
              vm.gender = data.gender;
              return;
            }

            vm.gender = 'Other';
            vm.genderSpecify = data.gender;
          });
        });
    },
  };
</script>

