<template>
  <Nav />
  <div class="app-container">
    <div class="faq-container">
      <h1>Frequently Asked Questions</h1>
      <div class="faq-item" v-for="faq in faqs" :key="faq.question">
        <h2 @click="toggleFAQ(faq)">{{ faq.question }}</h2>
        <p v-if="faq.open">{{ faq.answer }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import Nav from "@/components/NavigationBar1.vue";
import { ref } from 'vue';

const faqs = ref([
  {
    question: "How do I register for a tournament?",
    answer: "To register for a tournament, please go to the Tournaments page and click on the 'Register' button next to the tournament you wish to join." +
        "Please input your username in the 'Game name' section and your team name in the 'team name' section. If you are playing solo, please write None for teamname",
    open: false
  },
  {
    question: "Can I join multiple tournaments?",
    answer: "Yes, you can join as many tournaments as you like as long as you meet the eligibility criteria for each tournament.",
    open: false
  },
  {
    question: "How do I view my tournament registrations and tournaments?",
    answer: "You can view your tournament registrations on the Players data page after logging into your account.",
    open: false
  },
  {
    question: "How to create a tournament?",
    answer: "You can click on the 'Create Tournament' button in the Navigation bar. " +
        "Once there, please provide the name of the game, the maximum amount of competitors allowed AND the link to a private groupchat for further details on the game",
    open: false
  },
  {
    question: "Can I delete my tournaments/registration",
    answer: "You can delete your tournaments/registrations over on the Players Data page" +
        "We do not allow any edits to be made once a tournament/registration is done.",
    open: false
  },
  {
    question: "Any other issues?",
    answer: "Feel free to reach out to us as devya.sha@student.mahidol.edu. We'll get back to you asap",
    open: false
  }
]);

const toggleFAQ = (faq) => {
  faq.open = !faq.open;
};
</script>

<style scoped>
.app-container {
  background: url('@/assets/giphy.gif') no-repeat center center fixed;
  background-size: cover;
  height: 100vh;
  display: flex;
  flex-direction: column;
}
body {
  background: url('@/assets/360_F_624734667_gvD8jWqOyZN9PGuhJw4EOJZSt7aePMn6.jpg') no-repeat center center fixed;
  background-size: cover;
  margin: 0;
  padding: 0;
  height: 100%;
  overflow: auto;
}

.faq-container {
  background: rgba(255, 255, 255, 0.9);
  padding: 20px;
  border-radius: 10px;
  max-width: 800px;
  margin: 50px auto;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
}

.faq-container h1 {
  text-align: center;
  margin-bottom: 20px;
}

.faq-item {
  margin-bottom: 20px;
}

.faq-item h2 {
  background: #009879;
  color: white;
  padding: 10px;
  cursor: pointer;
  border-radius: 5px;
  transition: background 0.3s;
}

.faq-item h2:hover {
  background: #007a63;
}

.faq-item p {
  padding: 10px;
  background: #f3f3f3;
  border-radius: 5px;
}
</style>

