<template>
  <div class="container">
    <p class="field mb-20">
      <button @click="saveCode" class="button is-primary">
        Save
      </button>
      <button @click="copyCode" class="button is-info">
        Copy
      </button>
    </p>
    <div class="columns">
      <div class="column">
        <div class="box">
          <h2 class="is-size-4 mb-15">Code</h2>
          <div class="mb-15">
            <button class="button is-success" @click="runCode">Run</button>
            <button class="button is-danger" :disabled="!running" @click="stopCode">Stop</button>
          </div>
          <pre id="code">{{ initialCode }}</pre>
        </div>
      </div>
      <div class="column">
        <div class="box">
          <h2 class="is-size-4 mb-15">Display</h2>
          <div class="mb-15">
            <button class="button is-primary" @click="clearScreen">Clear Display</button>
          </div>
          <div class="preview">
            <canvas id="game" height="460" width="400"></canvas>
            <img id="gameBg" src="../../assets/building.png">
          </div>
        </div>
      </div>
    </div>
    <div>
      <div class="box">
        <h2 class="is-size-4 mb-15">Output</h2>
        <div class="mb-15">
          <button class="button is-primary" @click="clearConsole">Clear Output</button>
        </div>
        <pre id="outputLog"></pre>
      </div>
    </div>
    <b-modal :active.sync="isSaveAsModalActive">
      <div class="modal-card" style="width: auto">
        <header class="modal-card-head">
            <p class="modal-card-title">Save As</p>
        </header>
        <section class="modal-card-body">
          <form @submit.prevent="saveAs(); isSaveAsModalActive = false;">
            <b-field label="File Name">
                <b-input
                    type="text"
                    v-model="saveAsInput"
                    placeholder="file.py"
                    required>
                </b-input>
            </b-field>
            <div class="mt-20 has-text-centered">
              <button class="button is-success">Save</button>
            </div>
          </form>
        </section>
      </div>
    </b-modal>
  </div>
</template>

<script>
  import ace from 'brace';
  import 'brace/mode/python';
  import 'brace/theme/monokai';
  import 'brace/ext/language_tools';
  import { mapState } from 'vuex';

  import { save } from '../../api/editor';

  import empty from '../../assets/python/empty.py';
  import { SkulptRun, SkulptQuit, SkulptClearPrints, SkulptClearScreen } from '../../util/editorUtil';

  let editor;

  export default {
    props: ['code', 'name', 'loaded'],
    data() {
      return {
        running: false,
        saveAsInput: '',
        rename: null,
        isSaveAsModalActive: false,
      };
    },
    computed: {
      initialCode() {
        if (this.code) {
          return this.code;
        }

        return empty;
      },
      computedName() {
        return this.rename || this.name;
      },
      ...mapState([
        'user',
      ]),
    },
    mounted() {
      editor = ace.edit('code');
      editor.setTheme('ace/theme/monokai');
      editor.session.setMode('ace/mode/python');
      editor.setShowPrintMargin(false);
      editor.$blockScrolling = Infinity;
      editor.setOptions({
        enableBasicAutocompletion: true,
        enableLiveAutocompletion: true,
      });

      SkulptClearScreen();
    },
    destroyed() {
      editor.destroy();
    },
    watch: {
      code() {
        editor.setValue(this.code);
        this.stopCode();
        this.clearConsole();
        this.clearScreen();
      },
    },
    methods: {
      saveAs() {
        this.rename = this.saveAsInput;
        this.saveCode();
      },
      runCode() {
        SkulptRun(editor.getValue());
        this.running = true;
      },
      stopCode() {
        SkulptQuit();
        this.running = false;
      },
      clearConsole() {
        SkulptClearPrints();
      },
      clearScreen() {
        SkulptClearScreen();
      },
      saveCode() {
        if (!this.user) {
          this.$snackbar.open({
            message: 'Cannot save file. You aren\'t logged in!',
            type: 'is-danger',
          });
          return;
        }

        const vm = this;

        if (this.computedName === '') {
          this.isSaveAsModalActive = true;
          return;
        }

        save(this.computedName, editor.getValue())
          .then((response) => {
            if (!response.ok) {
              vm.$snackbar.open({
                message: 'An error occured when saving the file.',
                type: 'is-danger',
              });
              return;
            }

            vm.$snackbar.open({
              message: 'Your code has been saved!',
              type: 'is-success',
            });
          });
      },
      copyCode() {
        const prevSelection = editor.selection.toJSON();
        editor.selectAll();
        editor.focus();
        document.execCommand('copy');
        editor.selection.fromJSON(prevSelection);
      },
    },
  };
</script>

<style lang="scss" scoped>
  #code, .preview {
    height: 400px;
    border: 1px solid #DDD;
    border-radius: 4px;
  }

  .preview {
    position: relative;
    background: #1D1722;
    overflow: hidden;
  }

  #game {
    width: 190px;
    height: 230px;
    top: 70px;
    right: 93px;
    position: absolute;
    z-index: 2;
  }

  #gameBg {
    position: absolute;
    top: 0;
    bottom: 0;
    right: 0;
    height: 100%;
    width: 609px;
    max-width: unset;
  }

  #outputLog {
    height: 200px;
  }
</style>


