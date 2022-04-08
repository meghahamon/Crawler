function main() {
    $.get({
      url: 'http://127.0.0.1:5000/artists',
      success: (data) => {
        list = '';
        data.forEach((element) => {
          list +=
            `<li class="artistbox" value=${element.id}>` + element.name + `</li>`;
        });
        tag = `<h4>Artists</h4><ul>${list}</ul>`;
        $('div.artist').html(tag);
        // console.log(data);
      },
    });
    $(document).on('click', 'li.artistbox', function () {
      $.get({
        url: `http://127.0.0.1:5000/songs/${this.value}`,
        success: (data) => {
          list = '';
          data.forEach((element) => {
            list +=
              `<li class="songbox" id=${element.id}>` + element.name + `</li>`;
          });
          tag = `<h4>Songs</h4><ul type="none">${list}</ul>`;
          $('div.songlist').html(tag);
          // console.log(data);
        },
      });
    });
    $(document).on('click', 'li.songbox', function () {
      $.get({
        url: `http://127.0.0.1:5000/songs/${this.value}/lyrics/${this.id}`,
        success: (data) => {
          lyrics = `<h4 class="lhead">Lyrics</h4><pre><p>${data}</p></pre>`;
          $('div.lyrics').html(lyrics);
          // console.log(data);
        },
      });
    });
  }
  $(main);
  
     