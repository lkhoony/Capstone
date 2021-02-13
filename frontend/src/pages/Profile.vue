<template>
  <div class="row">
    <div class="col-md-8">
      <edit-profile-form>
      </edit-profile-form>
    </div>
    <div class="col-md-4">
      <user-card></user-card>
    </div>
  </div>
</template>
<script>
  import EditProfileForm from './Profile/EditProfileForm';
  import UserCard from './Profile/UserCard'
  export default {
    components: {
      EditProfileForm,
      UserCard
    }
  }
</script>
<style>
</style>
