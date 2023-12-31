<template>
  <v-app class="hau hau--app">
    <!-- Application bar -->
    <v-app-bar app color="black" dark elevation="0">
      <div class="d-flex align-center">
        <v-tooltip bottom :disabled="isMobile">
          <template v-slot:activator="{ on, attrs }">
            <v-img
              class="shrink mr-2 hau hau-logo"
              contain
              v-bind="attrs"
              v-on="on"
              src="imgs/logo.svg"
              transition="scale-transition"
              width="32"
              @click.native="onLogoClick"
            />
          </template>
          <span>Intelligent Tutoring System</span>
        </v-tooltip>
      </div>
      <v-spacer></v-spacer>
      <v-tooltip
        bottom
        v-for="item in items"
        :key="item.title"
        :disabled="isMobile"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn dark icon v-bind="attrs" v-on="on" :to="item.route">
            <v-icon>{{ item.icon }}</v-icon>
          </v-btn>
        </template>
        <span> {{ item.title }} </span>
      </v-tooltip>
    </v-app-bar>
    <!-- Router -->
    <v-main :class="'hau hau-main-view' + (isHomePage ? ' home-page' : '')">
      <router-view />
    </v-main>
    <ChatbotModal />
    <v-tooltip left :disabled="isMobile">
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          class="mx-2"
          fab
          dark
          x-large
          color="#313135"
          v-bind="attrs"
          v-on="on"
          bottom
          right
          fixed
          @click="onChatbotClicked"
        >
          <ChatbotIcon class="hau hau-chatbot-icon" />
        </v-btn>
      </template>
      <span>Learning assistant John</span>
    </v-tooltip>
  </v-app>
</template>

<script>
import ChatbotModal from "./components/ChatbotModal.vue";
import ChatbotIcon from "./icons/ChatbotIcon.vue";

export default {
  name: "App",
  components: {
    ChatbotModal,
    ChatbotIcon,
  },
  data: () => ({
    items: [
      { title: "Home", icon: "mdi-home", route: "/" },
      { title: "Courses", icon: "mdi-book", route: "/courses" },
      // { title: "Our Team", icon: "mdi-account-group-outline", route: "/team" },
      // {
      //   title: "About Us",
      //   icon: "mdi-information-outline",
      //   route: "/about",
      // },
    ],
    drawer: true,
    mini: true,
  }),
  computed: {
    fullName() {
      if (this.$store) {
        return this.$store.getters.fullName;
      }

      return "";
    },
    isMobile() {
      let bpName = this.$vuetify.breakpoint.name;

      return bpName === "xs" || bpName === "sm";
    },
    isHomePage() {
      return this.$route.path === "/";
    },
  },
  methods: {
    onLogoClick() {
      this.$router.push({
        path: "/",
      });
    },
    onChatbotClicked() {
      this.$store.dispatch("openChatbot");
    },
  },
  mounted() {
    setInterval(() => {
      this.mini = true;
      this.drawer = true;
    }, 3000);
  },
};
</script>

<style lang="scss">
.hau.hau--app {
  .hau.hau-main-view {
    padding-top: 72px !important;

    &.home-page {
      padding-top: 42px !important;
    }
  }

  .container.hau {
    padding: 0 8px;
  }
}

.hau.hau-chatbot-icon {
  min-width: 96px;
  margin-bottom: 32px;
}

.hau.hau-logo {
  cursor: pointer;
}

@media (min-width: 960px) {
  .hau.hau--app {
    padding-top: 48px;

    .hau.hau-main-view {
      padding-top: 24px !important;

      &.home-page {
        padding-top: 0 !important;
      }
    }

    .container.hau {
      padding: 12px;
    }
  }
}
</style>
