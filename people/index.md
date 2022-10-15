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

## Ph.D. Students

{%
  include list.html
  data="members"
  component="portrait"
  filters="role: phd"
%}

## Master Students

{%
  include list.html
  data="members"
  component="portrait"
  filters="role: master"
%}

{% include section.html %}

## PostDocs

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

<!-- {%
  include list.html
  data="alumni"
  component="portrait"
  filters="role: pi"
%} -->

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
<!-- {%
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
%} -->
<!-- {:.center} -->
