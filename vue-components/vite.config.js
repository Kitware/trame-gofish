export default {
  base: "./",
  build: {
    lib: {
      entry: "./src/main.js",
      name: "trame_gofish",
      formats: ["umd"],
      fileName: "trame_gofish",
    },
    rollupOptions: {
      external: ["vue"],
      output: {
        globals: {
          vue: "Vue",
        },
      },
    },
    outDir: "../src/trame_gofish/module/serve",
    assetsDir: ".",
  },
};
