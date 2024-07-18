<template>
  <Nav />
  <div class="app-container">
    <main class="form-signin w-100 m-auto">
    <h2>Creating a tournament</h2>
    <form @submit.prevent="save">
      <div class="form-group">
        <label>Game Name: </label>
        <input type="text" v-model="tournament.gamename" class="form-control" placeholder="Game Name">
      </div>
      <div class="form-group">
        <label>Username: </label>
        <input type="text" v-model="tournament.participantnumber" class="form-control" placeholder="Username" readonly>
      </div>
      <div class="form-group">
        <label>Game Link: </label>
        <input type="text" v-model="tournament.gamelink" class="form-control" placeholder="Game Link">
      </div>
      <div class="form-group">
        <label>Max users: </label>
        <input type="text" v-model="tournament.totaluser" class="form-control" placeholder="Game Link">
      </div>
      <p> </p>
      <button type="submit" class="button1">Save</button>
    </form>
    </main>
  </div>
</template>

<script>
import axios from 'axios';
import Nav from "@/components/NavigationBar1.vue";
import { useStore } from 'vuex';
import { computed } from 'vue';

export default {
  components: { Nav },
  data() {
    return {
      tournament: {
        listID: '',
        gamename: '',
        participantnumber: '',
        teamname: '',
        gamelink: '',
        totaluser: ''
      }
    }
  },
  setup() {
    const store = useStore();
    const customername = computed(() => store.state.customer.customername);
    return { customername };
  },
  created() {
    this.tournament.participantnumber = this.customername;
  },
  methods: {
    save() {
      axios.post("http://localhost:8080/api/v1/gamelist/save", this.tournament)
          .then(({ data }) => {
            alert("Saved successfully");
            this.resetForm();
          })
          .catch(error => {
            console.error('Error saving tournament:', error);
            alert('Failed to save tournament');
          });
    },
    resetForm() {
      this.tournament.listID = '';
      this.tournament.gamename = '';
      this.tournament.participantnumber = '';
      this.tournament.teamname = '';
      this.tournament.gamelink = '';
      this.tournament.totaluser = '';
    }
  }
}
</script>

<style scoped>
.app-container {
  background: url('@/assets/7f4e7533-7c29-47d2-816b-831cd53649a5_text.gif') no-repeat center center fixed;
  background-size: cover;
  height: 100vh;
  display: flex;
  flex-direction: column;
}
.button1 {
  background-color: green;
  border: none;
  color: white;
  padding: 5px 10px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 12px;
}
.form-signin {
  background-color: orange;
  max-width: 330px;
  padding: 15px;
  margin: auto;
  background: rgba(255, 255, 255, 0.8);
  border-radius: 10px;
  margin-top: 100px;
}

.form-signin {
  background-color: orange;
  max-width: 330px;
  padding: 15px;
  margin: auto;
}

</style>
