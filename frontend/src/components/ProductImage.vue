<template>
<article class="gallery-wrap">
  <div class="img-big-wrap">
    <div>
      <a href="#">
        <img :src='src' alt="Image not available..." class="img-fluid">
      </a>
    </div>
  </div>
</article>
</template>

<script>
export default {
  name: 'ProductImage',
  props: ['product'],
  data: function () {
    return {
      src: this.product.thumbnail
    }
  }
}
</script>

<style>
.gallery-wrap .img-big-wrap img {
    height: 450px;
    width: auto;
    display: inline-block;
    cursor: zoom-in;
}
.gallery-wrap .img-small-wrap .item-gallery {
    width: 60px;
    height: 60px;
    border: 1px solid #ddd;
    margin: 7px 2px;
    display: inline-block;
    overflow: hidden;
}
.gallery-wrap .img-small-wrap {
    text-align: center;
}
.gallery-wrap .img-small-wrap img {
    max-width: 100%;
    max-height: 100%;
    object-fit: cover;
    border-radius: 4px;
    cursor: zoom-in;
}
</style>
