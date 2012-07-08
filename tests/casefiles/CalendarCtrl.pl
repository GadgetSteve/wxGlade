#!/usr/bin/perl -w -- 
#
# generated by wxGlade "faked test version"
#
# To get wxPerl visit http://wxPerl.sourceforge.net/
#

use Wx 0.15 qw[:allclasses];
use strict;

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade

package MyDialog;

use Wx qw[:everything];
use base qw(Wx::Dialog);
use strict;

sub new {
        my( $self, $parent, $id, $title, $pos, $size, $style, $name ) = @_;
        $parent = undef              unless defined $parent;
        $id     = -1                 unless defined $id;
        $title  = ""                 unless defined $title;
        $pos    = wxDefaultPosition  unless defined $pos;
        $size   = wxDefaultSize      unless defined $size;
        $name   = ""                 unless defined $name;

        # begin wxGlade: MyDialog::new

        $style = wxDEFAULT_DIALOG_STYLE 
                unless defined $style;

        $self = $self->SUPER::new( $parent, $id, $title, $pos, $size, $style, $name );
        $self->{calendar_ctrl_1} = Wx::CalendarCtrl->new($self, wxID_ANY, Wx::DateTime->new, wxDefaultPosition, wxDefaultSize, );

        $self->__set_properties();
        $self->__do_layout();

        # end wxGlade
        return $self;

}


sub __set_properties {
        my $self = shift;

        # begin wxGlade: MyDialog::__set_properties

        $self->SetTitle("dialog_1");

        # end wxGlade
}

sub __do_layout {
        my $self = shift;

        # begin wxGlade: MyDialog::__do_layout

        $self->{sizer_1} = Wx::BoxSizer->new(wxHORIZONTAL);
        $self->{sizer_1}->Add($self->{calendar_ctrl_1}, 0, 0, 0);
        $self->SetSizer($self->{sizer_1});
        $self->{sizer_1}->Fit($self);
        $self->Layout();

        # end wxGlade
}

# end of class MyDialog

1;

1;

package main;

unless(caller){
        local *Wx::App::OnInit = sub{1};
        my $app = Wx::App->new();
        Wx::InitAllImageHandlers();

        my $dialog_1 = MyDialog->new();

        $app->SetTopWindow($dialog_1);
        $dialog_1->Show(1);
        $app->MainLoop();
}
