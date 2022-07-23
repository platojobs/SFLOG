# [12云：pod-install出现警告ruby的警告](https://github.com/platojobs/SFLOG/issues/12)

>  `warning: Using the last argument as keyword parameters is deprecated; maybe ** should be added to the call`


#### 1. `pod install`出现下面的问题👇,脚本用`zsh`

```
/Users/gitartos/.rvm/rubies/ruby-2.7.0/lib/ruby/gems/2.7.0/gems/nanaimo-0.2.6/lib/nanaimo/writer/pbxproj.rb:13: warning: Using the last argument as keyword parameters is deprecated; maybe ** should be added to the call
/Users/gitartos/.rvm/rubies/ruby-2.7.0/lib/ruby/gems/2.7.0/gems/nanaimo-0.2.6/lib/nanaimo/writer.rb:35: warning: The called method `initialize' is defined here
Integrating client project

```
其实是ruby的问题

#### 2. 在你的`~/.zshrc`文件中加入下面配置：

```
export RUBYOPT=-W0

```
保存起来；
#### 3. Try to reload` ZSH `config by typing,就可以了。
使配置生效，再`pod install`,那就完美了，没出现`<**1**>`的问题了;

```
Generating Pods project
Integrating client project
Pod installation complete! There are 4 dependencies from the Podfile and 4 total pods installed.

```
