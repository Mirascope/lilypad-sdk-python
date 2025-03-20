# Changelog

## 0.1.0-alpha.1 (2025-03-20)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/Mirascope/lilypad-sdk-python/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** update via SDK Studio ([a5b310c](https://github.com/Mirascope/lilypad-sdk-python/commit/a5b310c877d165da34a419cec22e812061796740))
* **api:** update via SDK Studio ([5f118a2](https://github.com/Mirascope/lilypad-sdk-python/commit/5f118a27674c63d1e2696e7bba312248ac4719c4))
* **api:** update via SDK Studio ([b493b2d](https://github.com/Mirascope/lilypad-sdk-python/commit/b493b2d898d30ff41ba43d0371ec6672e39bc783))
* **api:** update via SDK Studio ([cc6d220](https://github.com/Mirascope/lilypad-sdk-python/commit/cc6d2204bc53813de18ec5b3b8d3604ae350b150))
* **api:** update via SDK Studio ([db87970](https://github.com/Mirascope/lilypad-sdk-python/commit/db87970e81ae8dd2fc503b7b62cb0a06945e201f))
* **api:** update via SDK Studio ([6452d5f](https://github.com/Mirascope/lilypad-sdk-python/commit/6452d5f711ae076021c49154c329d4b47ade4150))
* **api:** update via SDK Studio ([e431b2e](https://github.com/Mirascope/lilypad-sdk-python/commit/e431b2e52c418a7d8f16d47cf86a242d440d9c74))
* **api:** update via SDK Studio ([9940c00](https://github.com/Mirascope/lilypad-sdk-python/commit/9940c00722028375c2948b14cd1a8c2f15aa58c2))
* **api:** update via SDK Studio ([#4](https://github.com/Mirascope/lilypad-sdk-python/issues/4)) ([81abe90](https://github.com/Mirascope/lilypad-sdk-python/commit/81abe90d26a8a40884e532b43301735cd3332e86))
* **client:** send retry count header ([14824ef](https://github.com/Mirascope/lilypad-sdk-python/commit/14824efc0fe5773ff3bbc5384f66d2c1afe8b187))


### Bug Fixes

* **client:** compat with new httpx 0.28.0 release ([4858d80](https://github.com/Mirascope/lilypad-sdk-python/commit/4858d80775a175d43bc22ae70994714b08f55103))
* **client:** handle domains with underscores ([436a32a](https://github.com/Mirascope/lilypad-sdk-python/commit/436a32a1a9127ad620022d9960400c5499182e19))
* **client:** only call .close() when needed ([776bfc1](https://github.com/Mirascope/lilypad-sdk-python/commit/776bfc10afd098183b5bd1426e7e204c9549d0e0))
* correctly handle deserialising `cls` fields ([9bc9939](https://github.com/Mirascope/lilypad-sdk-python/commit/9bc993920032995128cdc1c2d65f713bb725a8ce))
* **tests:** make test_get_platform less flaky ([be5c71c](https://github.com/Mirascope/lilypad-sdk-python/commit/be5c71c4cf5473e9826afe3c539e645f89c40163))


### Chores

* add missing isclass check ([079adee](https://github.com/Mirascope/lilypad-sdk-python/commit/079adee835d90001b54c61e22e7227c18721967e))
* configure new SDK language ([51a325c](https://github.com/Mirascope/lilypad-sdk-python/commit/51a325c6cc974d3fba6811652f08d0f4ea703bbd))
* fix cyclical imports ([048f2de](https://github.com/Mirascope/lilypad-sdk-python/commit/048f2def739df98f1037fe3e8a3af04bcf3cc5a9))
* go live ([#1](https://github.com/Mirascope/lilypad-sdk-python/issues/1)) ([a704447](https://github.com/Mirascope/lilypad-sdk-python/commit/a704447f91a25d38bbdc734aaaa1eb9fd2b0c306))
* **internal:** add support for parsing bool response content ([a60ac00](https://github.com/Mirascope/lilypad-sdk-python/commit/a60ac00e1e63462414e0994c7705eed8c5c65d77))
* **internal:** add support for TypeAliasType ([37a4237](https://github.com/Mirascope/lilypad-sdk-python/commit/37a42373380116735e8be345101a150107a38a2a))
* **internal:** avoid pytest-asyncio deprecation warning ([e0909dc](https://github.com/Mirascope/lilypad-sdk-python/commit/e0909dcc30d0e201a40470cb06fb24ce1c565e5c))
* **internal:** bump httpx dependency ([5b78027](https://github.com/Mirascope/lilypad-sdk-python/commit/5b780270dd211e727c55b16a42cc71521e3ab064))
* **internal:** bump pydantic dependency ([347ef4e](https://github.com/Mirascope/lilypad-sdk-python/commit/347ef4e574105271ec45c333d2d77c2aefae999c))
* **internal:** bump pyright ([dc215c8](https://github.com/Mirascope/lilypad-sdk-python/commit/dc215c8db5a474b66ff611113daafad91048e5ef))
* **internal:** bump pyright ([e4b9d2b](https://github.com/Mirascope/lilypad-sdk-python/commit/e4b9d2b8d4a6ddad345e0e451f051ecec5ea4454))
* **internal:** codegen related update ([0aa38cf](https://github.com/Mirascope/lilypad-sdk-python/commit/0aa38cf1d128c70a013c7c6c0bc32f42ed275b01))
* **internal:** codegen related update ([6c25896](https://github.com/Mirascope/lilypad-sdk-python/commit/6c25896f975c097445dda6e511c0b674c50c61d1))
* **internal:** codegen related update ([6c9d326](https://github.com/Mirascope/lilypad-sdk-python/commit/6c9d3265ea55449604e0f9ac9a84a4db68d783c2))
* **internal:** codegen related update ([8670519](https://github.com/Mirascope/lilypad-sdk-python/commit/86705196ca3bcc30e2143c2d3c9c6c401ad0a6ee))
* **internal:** codegen related update ([02d6978](https://github.com/Mirascope/lilypad-sdk-python/commit/02d69786985ff6ef7e6f9fe3862428197f098d4e))
* **internal:** codegen related update ([720364b](https://github.com/Mirascope/lilypad-sdk-python/commit/720364b22aced3f892072017dbec915f55405937))
* **internal:** codegen related update ([0671e3e](https://github.com/Mirascope/lilypad-sdk-python/commit/0671e3e32af17c7a9e816f9f8f2cf56e6e0a6504))
* **internal:** codegen related update ([e97778e](https://github.com/Mirascope/lilypad-sdk-python/commit/e97778e17088a766bcaff0c4e8ea3cb991eac090))
* **internal:** codegen related update ([9f5789f](https://github.com/Mirascope/lilypad-sdk-python/commit/9f5789f184ebc73e28644641121fe9ff67a40ee6))
* **internal:** codegen related update ([d5bdd81](https://github.com/Mirascope/lilypad-sdk-python/commit/d5bdd8130331fe86b175fe550821862cff791182))
* **internal:** codegen related update ([b60c3a2](https://github.com/Mirascope/lilypad-sdk-python/commit/b60c3a201f0e19bdcbc1aaa3edf58212bddb7a2e))
* **internal:** exclude mypy from running on tests ([30c3ff8](https://github.com/Mirascope/lilypad-sdk-python/commit/30c3ff80293324fdf02df4f3f1d3bb7efde38fdb))
* **internal:** fix compat model_dump method when warnings are passed ([355ecae](https://github.com/Mirascope/lilypad-sdk-python/commit/355ecae3f5b94e5bd7f5eaaffd04332da5db619c))
* **internal:** fix some typos ([a0deab4](https://github.com/Mirascope/lilypad-sdk-python/commit/a0deab4d2d693a93b814e9e85bfdfb2b52570f02))
* **internal:** minor formatting changes ([1ca3b4b](https://github.com/Mirascope/lilypad-sdk-python/commit/1ca3b4b57ff57332b6b5057e43899fa0d025ae3d))
* **internal:** minor style changes ([195e9f5](https://github.com/Mirascope/lilypad-sdk-python/commit/195e9f5c9a663f5c9d6800ca59d8b6620ab11376))
* **internal:** updated imports ([6630a2f](https://github.com/Mirascope/lilypad-sdk-python/commit/6630a2f51bca333c7af2865c7af43c04a67e9b62))
* make the `Omit` type public ([a3e1875](https://github.com/Mirascope/lilypad-sdk-python/commit/a3e18759a5328666477f3da067d55341a244e0d5))
* rebuild project due to codegen change ([0b52886](https://github.com/Mirascope/lilypad-sdk-python/commit/0b52886a87ed275efc889cef0494062edfb75c5f))
* rebuild project due to codegen change ([5a93c6b](https://github.com/Mirascope/lilypad-sdk-python/commit/5a93c6bf9438d6c6c0454e02df6f02dbc5030a02))
* rebuild project due to codegen change ([130235e](https://github.com/Mirascope/lilypad-sdk-python/commit/130235eb791325fda13064b6e5964c8328108b19))
* rebuild project due to codegen change ([16407e2](https://github.com/Mirascope/lilypad-sdk-python/commit/16407e28881de3086ac3500f9829173d9941317b))
* remove now unused `cached-property` dep ([3c24d2c](https://github.com/Mirascope/lilypad-sdk-python/commit/3c24d2c812d1f53de5f60cefc03576dbf972b726))
* update SDK settings ([#3](https://github.com/Mirascope/lilypad-sdk-python/issues/3)) ([4c34f20](https://github.com/Mirascope/lilypad-sdk-python/commit/4c34f20fb2f752aee08c8f456c2b459622450368))


### Documentation

* add info log level to readme ([9806034](https://github.com/Mirascope/lilypad-sdk-python/commit/980603434868e60fb859afb2144a67dc8c148c89))
* fix typos ([f31f724](https://github.com/Mirascope/lilypad-sdk-python/commit/f31f7244222329090c51c32463904cbcc42deec0))
* **raw responses:** fix duplicate `the` ([607f40f](https://github.com/Mirascope/lilypad-sdk-python/commit/607f40fb74e62331f310943f0594cd4d5a2a3ba8))
* **readme:** example snippet for client context manager ([6e95277](https://github.com/Mirascope/lilypad-sdk-python/commit/6e952776c826092ed999ab8d2c94c837da3ea6a3))
* **readme:** fix http client proxies example ([113f629](https://github.com/Mirascope/lilypad-sdk-python/commit/113f62910c2bd0f32765dbc4039b01692c4251a9))
