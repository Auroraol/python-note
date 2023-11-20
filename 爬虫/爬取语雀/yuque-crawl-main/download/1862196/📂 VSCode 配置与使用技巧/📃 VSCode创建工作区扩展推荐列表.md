在我们创建项目的时候，可能需要其他人协同编程，这时可能每个人的VSCode安装的扩展不一致，导致工作效率慢。

为此，我们可以创建工作区配置文件，将必要的扩展推荐放进去。<br />![Pasted image 20220623140056.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1655966120328-4d2315b4-7a1d-46b1-a9ba-3fbe5002e93f.png#clientId=u2b9e1927-4e76-4&from=drop&id=u5fd18d7b&originHeight=66&originWidth=229&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2694&status=done&style=none&taskId=ua9821f50-0512-4561-b4df-c2599f12455&title=)

这时项目级的配置，不要将`.vscode`目录添加到`.gitignore`中，以确保配置文件能够正常提交。

其中`extension.json`就是我们配置推荐扩展的地方。<br />示例：
```json
{
  "recommendations": [
    "antfu.iconify",
    "antfu.unocss",
    "antfu.vite",
    "antfu.goto-alias",
    "csstools.postcss",
    "dbaeumer.vscode-eslint",
    "vue.volar",
    "lokalise.i18n-ally",
    "streetsidesoftware.code-spell-checker"
  ]
}
```

`recommendations`中配置的是扩展的ID。如果不知道扩展的ID，可以在扩展详情中复制扩展ID获取。<br />![Pasted image 20220623143207.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1655966130832-19e6edb5-a8f6-48b4-8266-e7fe56f280ae.png#clientId=u2b9e1927-4e76-4&from=drop&id=uc66d0467&originHeight=343&originWidth=604&originalType=binary&ratio=1&rotation=0&showTitle=false&size=47475&status=done&style=none&taskId=ub858a0ca-b723-496b-b8c0-29512149101&title=)

这样，在项目中的扩展搜索框中输入`@recommended` 就可以看到配置的扩展推荐列表。<br />![Pasted image 20220623140620.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1655966136508-d1e7fcac-c44d-4d7f-8878-240addeede2e.png#clientId=u2b9e1927-4e76-4&from=drop&id=u4cea93f5&originHeight=746&originWidth=400&originalType=binary&ratio=1&rotation=0&showTitle=false&size=90630&status=done&style=none&taskId=u24c97820-02be-47b7-8306-9b57dd456c4&title=)

光安装好扩展不够，如果每个开发者对扩展的配置不一致，也可能导致扩展行为不一致或者出问题。

因此，还需要添加`settings.json`文件：
```json
{
  "cSpell.words": ["Vitesse", "Vite", "unocss", "vitest", "vueuse", "pinia", "demi", "antfu", "iconify", "intlify", "vitejs", "unplugin", "pnpm"],
  "i18n-ally.sourceLanguage": "en",
  "i18n-ally.keystyle": "nested",
  "i18n-ally.localesPaths": "locales",
  "i18n-ally.sortKeys": true,
  "prettier.enable": false,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  },
  "files.associations": {
    "*.css": "postcss"
  },
  "editor.formatOnSave": false
}
```

这样，协作开发者在下载好项目，安装依赖，安装推荐的扩展之后，VSCode可以达到一致的编辑体验。



