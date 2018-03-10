from django.views.generic import TemplateView

from vivalviar.core.models import Banner, Sponsor, SpecialParticipation, Photo, PlayList


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['banner_list'] = Banner.objects.all()
        context['sponsor_list'] = Sponsor.objects.all()
        return context


home = HomePageView.as_view()

history = TemplateView.as_view(
    template_name="history.html"
)


class SpecialParticipationPageView(TemplateView):
    template_name = "special_participation.html"

    def get_context_data(self, **kwargs):
        context = super(SpecialParticipationPageView, self).get_context_data(**kwargs)
        context['special_participation_list'] = SpecialParticipation.objects.all()
        return context


special_participation = SpecialParticipationPageView.as_view()


class PhotosPageView(TemplateView):
    template_name = "photos.html"

    def get_context_data(self, **kwargs):
        context = super(PhotosPageView, self).get_context_data(**kwargs)
        context['photo_list'] = Photo.objects.all()
        return context

photos = PhotosPageView.as_view()


class PlayListPageView(TemplateView):
    template_name = "videos.html"

    def get_context_data(self, **kwargs):
        context = super(PlayListPageView, self).get_context_data(**kwargs)
        context['playlist_list'] = PlayList.objects.all()
        return context


playlist = PlayListPageView.as_view()


contact_us = TemplateView.as_view(
    template_name="contact_us.html"
)
