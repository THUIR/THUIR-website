---
title: People
nav:
  order: 1
  tooltip: 团队成员
---

# <i class="fas fa-users"></i>Current

{% include section.html %}

## Professors

{%
  include list.html
  data="members"
  component="portrait"
  filters="role: pi"
%}

{% include section.html %}

{%
  include list.html
  data="members"
  component="portrait"
  filters="role: phd"
%}
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: master"
%}

{% include section.html %}

{%
  include list.html
  data="members"
  component="portrait"
  filters="role: postdoc"
%}

{% include section.html %}

{%
  include list.html
  data="members"
  component="portrait"
  filters="role: programmer"
%}
{:.center}

{% include section.html %}

# <i class="fas fa-users"></i>Alumni

{%
  include list.html
  data="alumni"
  component="portrait"
  filters="role: pi"
%}

{% include section.html %}

{%
  include list.html
  data="alumni"
  component="portrait"
  filters="role: phd"
%}
{%
  include list.html
  data="alumni"
  component="portrait"
  filters="role: master"
%}
{%
  include list.html
  data="alumni"
  component="portrait"
  filters="role: postdoc"
%}
{%
  include list.html
  data="alumni"
  component="portrait"
  filters="role: programmer"
%}
{:.center}


{% include section.html background="images/banner.jpg" dark=true%}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

{% include section.html %}

## Join

#### Post Dogtoral Researcher

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

- 3+ (dog) years experience managing bone portfolios
- Strong desire to learn tricks and go on walkies
- Aptitude to sit and stay

{% include link.html type="external" link="https://google.com/" text="Apply Now" icon="" style="button" %}
{:.center}

{% include section.html %}

## Funding

Our work is made possible by funding from several organizations.
{:.center}

{%
  include gallery.html
  style="square"

  image1="images/photo.jpg"
  link1="https://nasa.gov/"
  tooltip1="Cool Foundation"

  image2="images/photo.jpg"
  link2="https://nasa.gov/"
  tooltip2="Cool Institute"

  image3="images/photo.jpg"
  link3="https://nasa.gov/"
  tooltip3="Cool Initiative"

  image4="images/photo.jpg"
  link4="https://nasa.gov/"
  tooltip4="Cool Foundation"

  image5="images/photo.jpg"
  link5="https://nasa.gov/"
  tooltip5="Cool Institute"

  image6="images/photo.jpg"
  link6="https://nasa.gov/"
  tooltip6="Cool Initiative"
%}
