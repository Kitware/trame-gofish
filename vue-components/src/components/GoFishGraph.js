import * as gf from "gofish-graphics";
import { watch, ref } from "vue";

export default {
  emits: ["update"],
  props: {
    data: {
      type: Object,
    },
  },
  setup(props, { emit }) {
    const el = ref(null);

    function update([el, data]) {
      if (!el || !data) {
        return;
      }
      el.innerHTML = "";
      emit("update", { data, el, gf });
    }
    watch(() => [el.value, props.data], update);
    return { el };
  },
  template: '<div class="goFishGraph" ref="el"></div>',
};
