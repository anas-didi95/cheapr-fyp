<template>
<header id="header" class="header">
  <div class="header-menu">
    <div class="col-sm-7">
      <a id="menuToggle" class="menutoggle pull-left">
        <i class="fa fa fa-tasks"></i>
      </a>
      <div class="header-left">
        <h3>{{ title }}</h3>
      </div>
    </div>
    <div class="col-sm-5">
      <div class="user-area dropdown float-right">
        <a href="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          <img class="user-avatar rounded-circle" :src="userAvatar" alt="User Avatar">
        </a>
        <div class="user-menu dropdown-menu" x-placement="bottom-start" style="position: absolute; transform: translate3d(-88px, 0px, 0px); top: 0px; left: 0px; will-change: transform;">
          <a class="nav-link" href="#">
            <i class="fa fa- user"></i>My Profile</a>

          <a class="nav-link" href="#">
            <i class="fa fa- user"></i>Notifications
            <span class="count">13</span>
          </a>
          <a class="nav-link" href="#">
            <i class="fa fa -cog"></i>Settings</a>
          <a class="nav-link" href="#">
            <i class="fa fa-power -off"></i>Logout</a>
        </div>
      </div>
    </div>
  </div>
</header>
</template>

<script>
import UserAvatar from '@/assets/images/user.png'
export default {
  name: 'Header',
  props: ['title'],
  data: function () {
    return {
      userAvatar: UserAvatar
    }
  }
}
</script>

<style>

</style>
