<template>
  <Nav />
  <body>
  <div class="app-container">
    <h2>My registrations</h2>
    <table class="styled-table">
      <thead>
      <tr>
        <th scope="col">Tournament ID</th>
        <th scope="col">In Game Name</th>
        <th scope="col">Username</th>
        <th scope="col">Teamname</th>
        <th scope="col">Actions</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="tournament in tournaments" :key="tournament.gameID">
        <td>{{ tournament.category }}</td>
        <td>{{ tournament.name }}</td>
        <td>{{ tournament.username }}</td>
        <td>{{ tournament.teamname }}</td>
        <td>
          <button type="button" class="button1" @click="remove(tournament.gameID)">Delete</button>
        </td>
      </tr>
      </tbody>
    </table>

    <h2>My Tournaments </h2>
    <table class="styled-table">
      <thead>
      <tr>
        <th scope="col">List ID</th>
        <th scope="col">Game Link</th>
        <th scope="col">Game Name</th>
        <th scope="col">Username</th>
        <th scope="col">Total Users</th>
        <th scope="col">Actions</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="tournament in tournaments1" :key="tournament.listID">
        <td>{{ tournament.listID }}</td>
        <td><a :href="tournament.gamelink" target="_blank">{{ tournament.gamelink }}</a></td>
        <td>{{ tournament.gamename }}</td>
        <td>{{ tournament.participantnumber }}</td>
        <td>{{ tournament.totaluser }}</td>
        <td>
          <button type="button" class="button2" @click="getdata(tournament.listID)">Participants</button>
          <p> </p>
          <button type="button" class="button1" @click="remove1(tournament.listID)">Delete</button>
        </td>
      </tr>
      </tbody>
    </table>
  </div>
  </body>
</template>

<script>
import axios from 'axios';
import Nav from "@/components/NavigationBar1.vue";
import { useStore } from 'vuex';
import { computed } from 'vue';

export default {
  components: { Nav },
  setup() {
    const store = useStore();
    const customername = computed(() => store.state.customer.customername);
    return { customername };
  },
  data() {
    return {
      tournaments: [],
      tournaments1: [],
      currtourny: '',
      checkResult: ''
    };
  },
  created() {
    this.loadTournaments();
    this.loadTournaments1();
  },
  methods: {
    loadTournaments() {
      const username = this.customername;
      const url = `http://localhost:8080/api/v1/tournament/mytournaments/${username}`;
      axios.get(url)
          .then(({ data }) => {
            console.log(data);
            this.tournaments = data;
          })
          .catch(error => {
            console.error('Error loading tournaments:', error);
            alert('Failed to load tournaments');
          });
    },
    loadTournaments1() {
      const username = this.customername;
      const url = `http://localhost:8084/api/v1/gamelist/getcurrtournaments/${username}`;
      axios.get(url)
          .then(({ data }) => {
            console.log(data);
            this.tournaments1 = data;
          })
          .catch(error => {
            console.error('Error loading tournaments1:', error);
            alert('Failed to load tournaments1');
          });
    },
    getdata(gameID) {
      this.$router.push({ path: '/tournamentdata', query: { gameID } });
    },
    remove(gameID) {
      const url = `http://localhost:8084/api/v1/tournament/deleteTournament/${gameID}`;
      axios.delete(url)
          .then(() => {
            alert("Deleted successfully");
            this.loadTournaments();
          })
          .catch(error => {
            console.error('Error deleting tournament:', error);
            alert('Failed to delete tournament');
          });
    },
    remove1(listID) {
      const url = `http://localhost:8084/api/v1/gamelist/deletecustomer/${listID}`;
      axios.delete(url)
          .then(() => {
            alert("Deleted successfully");
            this.loadTournaments1();
          })
          .catch(error => {
            console.error('Error deleting tournament1:', error);
            alert('Failed to delete tournament1');
          });
    }
  }
}
</script>

<style scoped>
body {
  background: url('@/assets/a33tbu71hwxb1.gif') no-repeat center center fixed;
  background-size: cover;
  margin: 0;
  padding: 0;
  height: 100%;
  overflow: auto;
}

.app-container {
  background: rgba(255, 255, 255, 0.8); /* Add a semi-transparent background to the container */
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center; /* Centers horizontally */
  padding: 20px;
}

.styled-table {
  border-collapse: collapse;
  margin: 25px 0;
  font-size: 0.9em;
  font-family: sans-serif;
  min-width: 400px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
}

.form-signin {
  max-width: 330px;
  padding: 15px;
  margin: auto;
  background: rgba(255, 255, 255, 0.8);
  border-radius: 10px;
  margin-top: 100px;
}

.button1 {
  background-color: orange;
  border: none;
  color: black;
  padding: 5px 10px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 12px;
}

.button2 {
  background-color: lightblue;
  border: none;
  color: black;
  padding: 5px 10px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 12px;
}

.form-floating {
  margin-bottom: 15px;
}

.styled-table thead tr {
  background-color: #009879;
  color: #ffffff;
  text-align: left;
}

.styled-table th,
.styled-table td {
  padding: 12px 15px;
}

.styled-table tbody tr {
  border-bottom: 1px solid #dddddd;
}

.styled-table tbody tr:nth-of-type(even) {
  background-color: #f3f3f3;
}

.styled-table tbody tr:last-of-type {
  border-bottom: 2px solid #009879;
}

.styled-table tbody tr.active-row {
  font-weight: bold;
  color: #009879;
}
</style>
