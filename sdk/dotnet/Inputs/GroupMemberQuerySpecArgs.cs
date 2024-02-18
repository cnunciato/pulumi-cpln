// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Cpln.Inputs
{

    public sealed class GroupMemberQuerySpecArgs : global::Pulumi.ResourceArgs
    {
        [Input("match")]
        public Input<string>? Match { get; set; }

        [Input("terms")]
        private InputList<Inputs.GroupMemberQuerySpecTermArgs>? _terms;
        public InputList<Inputs.GroupMemberQuerySpecTermArgs> Terms
        {
            get => _terms ?? (_terms = new InputList<Inputs.GroupMemberQuerySpecTermArgs>());
            set => _terms = value;
        }

        public GroupMemberQuerySpecArgs()
        {
        }
        public static new GroupMemberQuerySpecArgs Empty => new GroupMemberQuerySpecArgs();
    }
}
