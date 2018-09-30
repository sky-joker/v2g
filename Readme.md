# v2g

This tool converts videos to high quality gif using ffmpeg.

## Requirement

* [ffmpeg](https://www.ffmpeg.org/)
* [ffmpeg-python](https://github.com/kkroening/ffmpeg-python)

## Instalattion

### example install ffmpeg by CentOS7

```
# rpm -ivh https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm
# yum -y install ffmpeg
```

### install v2g

```
$ git clone https://github.com/sky-joker/v2g.git
$ cd v2g
$ pip install -r requirements.txt
$ chmod +x v2g.py
```

## Usage

The following example converts a movie called `example.mov` to a high quality gif.

```
$ ./v2g.py -y -i example.mov -l high -o example
$ ls example.gif
example.gif
```

## License

[MIT](https://github.com/sky-joker/blob/master/LICENSE)

## Authour

[sky-joker](https://github.com/sky-joker)