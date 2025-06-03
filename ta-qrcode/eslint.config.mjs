const ignoreFiles = [];

const eslintRules = {
  semi: "error",
  "prefer-const": "error",
};

const eslintConfig = [
  {
    ignores: ignoreFiles,
    rules: eslintRules,
  },
];

export default eslintConfig;
